# UC2 Corpus Membership Freeze

Date: 2026-09-26
Phase: UC2-P4C

Eligibility criteria SHA256:
d35c735e88ff5c4a6a9241cc928e772d3a9940c453ef7ec20b93fe091b0c96ea

Eligibility review SHA256:
e04baf44698b848ed68cc5917ac86f258ef3c97b261a113eb2c09ce8c622043a

Pre-update global manifest SHA256:
9858ca4f656078add7e876d831a3551438672e1e978c218c8fe08522311133a1

Corpus membership SHA256:
e9b000a20d470b7cac52f232027f2a8ba9128ad41a92bb8b945b479997a37cc4

Post-update global manifest SHA256:
bd01315f1f6d035e4105ae4d89378c6df24af4d877411e9228a2fcf704368e89

Pre-freeze scope-contract SHA256:
c90b8884d916c83fd401fcb69965ff2c875ca8f593e40bcb30666c4dde141184

Post-freeze scope-contract SHA256:
fe7a4312744a5c043d6a26eada4a14ee6e067292acd9b7c64604ddd04b9867b9

Candidates: 18
Accepted: 17
Excluded: UC2-C14 / DOC054

The membership artifact had been created during the initial P4C attempt,
which then stopped before manifest mutation because an overly strict JSON
serialization guard used ASCII escaping. The existing repository manifest
was valid and unchanged. Continuation verified its established UTF-8
serialization and completed the binding without changing eligibility outcomes.

Membership was frozen before preprocessing, embeddings, retrieval
diagnostics, benchmark-task construction, or benchmark execution.

CORPUS_MEMBERSHIP_FROZEN=YES
RETRIEVAL_FOUNDATION_FROZEN=NO
BENCHMARK_STARTED=NO
