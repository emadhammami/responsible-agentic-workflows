"""Batch download verified PDF source documents."""

import argparse
import hashlib
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

from jsonschema import Draft202012Validator

from .manifest import load_corpus_manifest

DEFAULT_DOWNLOAD_SCHEMA = Path(
    "corpus/download_queue.schema.json"
)


def load_download_queue(
    queue_path: str | Path,
    *,
    schema_path: str | Path = DEFAULT_DOWNLOAD_SCHEMA,
) -> dict[str, object]:
    """Load and validate a PDF download queue."""

    queue = json.loads(
        Path(queue_path).read_text(encoding="utf-8")
    )

    schema = json.loads(
        Path(schema_path).read_text(encoding="utf-8")
    )

    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(queue)

    filenames = [
        document["target_filename"]
        for document in queue["documents"]
    ]

    if len(filenames) != len(set(filenames)):
        raise ValueError(
            "Duplicate target_filename in download queue"
        )

    urls = [
        document["pdf_url"]
        for document in queue["documents"]
    ]

    if len(urls) != len(set(urls)):
        raise ValueError(
            "Duplicate pdf_url in download queue"
        )

    return queue


def _download_pdf(
    url: str,
    destination: Path,
    *,
    timeout: int,
) -> dict[str, object]:
    request = Request(
        url,
        headers={
            "User-Agent": (
                "responsible-agentic-workflows/"
                "thesis-corpus-research"
            )
        },
    )

    with urlopen(
        request,
        timeout=timeout,
    ) as response:
        data = response.read()

        final_url = response.geturl()

    if len(data) < 1000:
        raise ValueError(
            f"Downloaded file is unexpectedly small: {url}"
        )

    if not data.startswith(b"%PDF-"):
        raise ValueError(
            f"Downloaded content is not a PDF: {url}"
        )

    destination.write_bytes(data)

    return {
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "final_url": final_url,
    }


def download_batch(
    queue_path: str | Path,
    *,
    manifest_path: str | Path = "corpus/manifest.json",
    schema_path: str | Path = DEFAULT_DOWNLOAD_SCHEMA,
    timeout: int = 60,
) -> list[dict[str, object]]:
    """Download one validated queue atomically."""

    manifest_path = Path(manifest_path)
    manifest = load_corpus_manifest(
        manifest_path
    )

    queue = load_download_queue(
        queue_path,
        schema_path=schema_path,
    )

    use_case_id = str(
        queue["use_case_id"]
    )

    known_use_cases = {
        str(use_case["use_case_id"])
        for use_case in manifest["use_cases"]
    }

    if use_case_id not in known_use_cases:
        raise ValueError(
            f"Unknown use_case_id: {use_case_id}"
        )

    repository_root = (
        manifest_path.resolve().parent.parent
    )

    raw_directory = (
        repository_root
        / "corpus"
        / "use_cases"
        / use_case_id
        / "raw"
    )

    raw_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    targets: list[
        tuple[dict[str, object], Path, Path]
    ] = []

    for entry in queue["documents"]:
        target = (
            raw_directory
            / str(entry["target_filename"])
        )

        temporary = target.with_name(
            f".{target.name}.part"
        )

        if target.exists():
            raise FileExistsError(
                f"Target already exists: {target}"
            )

        if temporary.exists():
            raise FileExistsError(
                f"Temporary target already exists: {temporary}"
            )

        targets.append(
            (
                entry,
                target,
                temporary,
            )
        )

    downloaded: list[
        tuple[dict[str, object], Path, Path, dict[str, object]]
    ] = []

    try:
        for entry, target, temporary in targets:
            result = _download_pdf(
                str(entry["pdf_url"]),
                temporary,
                timeout=timeout,
            )

            downloaded.append(
                (
                    entry,
                    target,
                    temporary,
                    result,
                )
            )

        for _, target, temporary, _ in downloaded:
            os.replace(
                temporary,
                target,
            )

    except Exception:
        for _, _, temporary in targets:
            temporary.unlink(
                missing_ok=True
            )

        raise

    return [
        {
            "title": entry["title"],
            "pdf_url": entry["pdf_url"],
            "target_path": (
                target
                .relative_to(repository_root)
                .as_posix()
            ),
            "final_url": result["final_url"],
            "bytes": result["bytes"],
            "sha256": result["sha256"],
        }
        for entry, target, _, result in downloaded
    ]


def main() -> None:
    """Download all PDFs in one queue."""

    parser = argparse.ArgumentParser(
        description=(
            "Download a validated batch of corpus PDFs."
        )
    )

    parser.add_argument(
        "queue_path",
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=60,
    )

    args = parser.parse_args()

    downloaded = download_batch(
        args.queue_path,
        timeout=args.timeout,
    )

    print(
        f"DOWNLOADED_COUNT={len(downloaded)}"
    )

    for document in downloaded:
        print(
            f'{document["target_path"]} | '
            f'{document["bytes"]} bytes | '
            f'{document["sha256"]}'
        )


if __name__ == "__main__":
    main()
