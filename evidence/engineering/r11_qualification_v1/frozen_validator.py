def valid(j,cid):
 try:
  assert set(j)=={"evaluation_id","correctness_score","correctness_reason",
   "abstention_outcome","claim_judgments","evaluator_notes"}
  assert j["evaluation_id"]==cid
  assert type(j["correctness_score"]) is int and j["correctness_score"] in (0,1,2)
  assert j["abstention_outcome"] in {"correct_abstention","failed_to_abstain","incorrect_abstention","not_applicable"}
  assert isinstance(j["correctness_reason"],str) and j["correctness_reason"].strip()
  assert isinstance(j["evaluator_notes"],str)
  assert isinstance(j["claim_judgments"],list)
  for x in j["claim_judgments"]:
   assert set(x)=={"claim_text","label","reason"}
   assert x["label"] in {"SUPPORTED","PARTIALLY_SUPPORTED","UNSUPPORTED","CONTRADICTED"}
   assert isinstance(x["claim_text"],str) and isinstance(x["reason"],str)
  return True
 except: return False
