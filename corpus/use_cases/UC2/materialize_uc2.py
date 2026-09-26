from pathlib import Path
from html.parser import HTMLParser
import argparse, csv, hashlib, json, re, subprocess, unicodedata

ROOT=Path("corpus/use_cases/UC2")
RAW=ROOT/"raw"

EXCLUDED={"script","style","noscript","svg","template",
          "nav","header","footer","form","aside"}

def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()

def sha_file(p):
    return sha_bytes(p.read_bytes())

def normalize(s):
    s=unicodedata.normalize("NFC",s)
    s=s.replace("\xa0"," ")
    return re.sub(r"\s+"," ",s).strip()

class Detector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.has_main=False
        self.has_body=False
    def handle_starttag(self,tag,attrs):
        tag=tag.lower()
        if tag=="main": self.has_main=True
        if tag=="body": self.has_body=True

class Extractor(HTMLParser):
    def __init__(self,root):
        super().__init__(convert_charrefs=True)
        self.root=root
        self.active=(root is None)
        self.root_seen=False
        self.skip=0
        self.parts=[]
    def handle_starttag(self,tag,attrs):
        tag=tag.lower()
        if self.root and tag==self.root and not self.root_seen:
            self.active=True
            self.root_seen=True
        if self.active and tag in EXCLUDED:
            self.skip+=1
    def handle_endtag(self,tag):
        tag=tag.lower()
        if self.active and tag in EXCLUDED and self.skip:
            self.skip-=1
        if self.root and tag==self.root and self.root_seen:
            self.active=False
    def handle_data(self,data):
        if self.active and self.skip==0:
            self.parts.append(data)

def html_text(path):
    raw=path.read_text(encoding="utf-8",errors="strict")
    d=Detector(); d.feed(raw)
    root="main" if d.has_main else ("body" if d.has_body else None)
    x=Extractor(root); x.feed(raw)
    return normalize(" ".join(x.parts))

def pdf_pages(path):
    info=subprocess.run(
        ["pdfinfo",str(path)],
        stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True
    ).stdout.decode("utf-8","strict")
    m=re.search(r"^Pages:\s+(\d+)",info,re.M)
    assert m, path
    return int(m.group(1))

def pdf_page_text(path,page):
    b=subprocess.run(
        ["pdftotext","-f",str(page),"-l",str(page),
         "-layout","-enc","UTF-8",str(path),"-"],
        stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True
    ).stdout
    return normalize(b.decode("utf-8","strict"))

def dump_line(obj):
    return json.dumps(
        obj,ensure_ascii=False,sort_keys=True,
        separators=(",",":")
    )

def main(out):
    out=Path(out)
    assert not out.exists()
    out.mkdir(parents=True)

    membership=json.loads((ROOT/"corpus_membership.json").read_text())
    meta=json.loads((ROOT/"acquisition_http_metadata.json").read_text())

    mapping=membership["candidate_document_mapping"]
    accepted=set(membership["accepted_document_ids"])
    assert "DOC054" not in accepted
    assert len(accepted)==17

    candidates=[
        c for c,d in mapping.items() if d in accepted
    ]
    candidates.sort(key=lambda c:int(mapping[c][3:]))

    units=[]
    chunks=[]
    docstats={}

    for cid in candidates:
        doc=mapping[cid]
        assert doc!="DOC054"

        components=meta[cid]
        unit_index=0
        doc_words=0
        doc_chunks=0

        for component_index,comp in enumerate(components,1):
            path=RAW/comp["file"]
            assert path.is_file()
            assert sha_file(path)==comp["sha256"]

            is_pdf=path.suffix.lower()==".pdf"

            items=[]
            if is_pdf:
                pages=pdf_pages(path)
                for page in range(1,pages+1):
                    items.append((page,pdf_page_text(path,page)))
            else:
                items.append((None,html_text(path)))

            for pdf_page,text in items:
                unit_index+=1
                words=text.split() if text else []
                doc_words+=len(words)

                suid=f"{doc}-U{unit_index:04d}"
                unit={
                    "schema_version":"0.1",
                    "use_case_id":"UC2",
                    "document_id":doc,
                    "candidate_id":cid,
                    "source_unit_id":suid,
                    "source_unit_index":unit_index,
                    "media_type":"pdf" if is_pdf else "html",
                    "source_component_path":comp["file"],
                    "source_component_index":component_index,
                    "source_component_sha256":comp["sha256"],
                    "pdf_page_number":pdf_page,
                    "source_url":comp.get("final_url") or comp["url"],
                    "text_sha256":sha_bytes(text.encode("utf-8")),
                    "word_count":len(words),
                    "text":text
                }
                units.append(unit)

                if not words:
                    continue

                start=0
                ci=0
                while start < len(words):
                    ci+=1
                    end=min(start+450,len(words))
                    txt=" ".join(words[start:end])

                    chunks.append({
                        "schema_version":"0.1",
                        "use_case_id":"UC2",
                        "chunk_id":f"{suid}-C{ci:04d}",
                        "document_id":doc,
                        "candidate_id":cid,
                        "source_unit_id":suid,
                        "source_unit_index":unit_index,
                        "chunk_index":ci,
                        "media_type":"pdf" if is_pdf else "html",
                        "source_component_path":comp["file"],
                        "source_component_index":component_index,
                        "pdf_page_number":pdf_page,
                        "source_url":comp.get("final_url") or comp["url"],
                        "start_word":start,
                        "end_word_exclusive":end,
                        "word_count":end-start,
                        "source_unit_text_sha256":unit["text_sha256"],
                        "text_sha256":sha_bytes(txt.encode("utf-8")),
                        "text":txt
                    })
                    doc_chunks+=1

                    if end==len(words):
                        break
                    start+=375

        docstats[doc]={
            "candidate_id":cid,
            "source_unit_count":unit_index,
            "normalized_word_count":doc_words,
            "chunk_count":doc_chunks
        }

    pdf_units=sum(x["media_type"]=="pdf" for x in units)
    html_units=sum(x["media_type"]=="html" for x in units)
    empty=sum(x["word_count"]==0 for x in units)

    assert len(units)==117, len(units)
    assert pdf_units==97, pdf_units
    assert html_units==20, html_units
    assert all(x["document_id"]!="DOC054" for x in units)
    assert all(x["document_id"]!="DOC054" for x in chunks)

    su=out/"source_units.jsonl"
    ch=out/"chunks.jsonl"

    su.write_text(
        "".join(dump_line(x)+"\n" for x in units),
        encoding="utf-8"
    )
    ch.write_text(
        "".join(dump_line(x)+"\n" for x in chunks),
        encoding="utf-8"
    )

    summary={
        "schema_version":"0.1",
        "use_case_id":"UC2",
        "materialization_config_sha256":
          sha_file(ROOT/"materialization_config.json"),
        "chunking_config_sha256":
          sha_file(ROOT/"chunking_config.json"),
        "corpus_membership_sha256":
          sha_file(ROOT/"corpus_membership.json"),
        "accepted_document_count":17,
        "excluded_document_ids":["DOC054"],
        "source_unit_count":len(units),
        "pdf_source_unit_count":pdf_units,
        "html_source_unit_count":html_units,
        "nonempty_source_unit_count":len(units)-empty,
        "empty_source_unit_count":empty,
        "chunk_count":len(chunks),
        "total_normalized_words":
          sum(x["word_count"] for x in units),
        "max_chunk_words":
          max((x["word_count"] for x in chunks),default=0),
        "per_document":docstats
    }

    (out/"materialization_summary.json").write_text(
        json.dumps(
            summary,indent=2,ensure_ascii=False,
            sort_keys=True
        )+"\n",
        encoding="utf-8"
    )

    print("DOCUMENTS=17")
    print("SOURCE_UNITS="+str(len(units)))
    print("PDF_SOURCE_UNITS="+str(pdf_units))
    print("HTML_SOURCE_UNITS="+str(html_units))
    print("EMPTY_SOURCE_UNITS="+str(empty))
    print("CHUNKS="+str(len(chunks)))
    print("TOTAL_NORMALIZED_WORDS="+str(summary["total_normalized_words"]))
    print("MAX_CHUNK_WORDS="+str(summary["max_chunk_words"]))

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True)
    main(ap.parse_args().output)
