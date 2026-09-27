# Primary Benchmark Configuration Freeze v0.1

Date: 2026-09-27

Implementation parent HEAD: `e3febd8fd0eb68dedf543519c7808d758132eedf`

Freeze ID: `PRIMARY-BENCHMARK-CONFIG-FREEZE-v0.1`

This is a prospective configuration freeze. At the parent HEAD, all three
primary UC configurations had status `working`. This implementation changed
only the top-level `status` value in each configuration to `frozen`; every
other configuration byte remains unchanged. No new scientific choice was made.

| Authoritative configuration | SHA256 after freeze |
| --- | --- |
| `benchmark/config/primary/benchmark-config-primary-uc1-v0.2.json` | `c9c1ecd06cd74bb8bf53c13c050d127d8af9cd439dc1c45e49d1498b6679a767` |
| `benchmark/config/primary/benchmark-config-primary-uc2-v0.2.json` | `770435ccbd835225e488a862e0abb51c1eb13e887e389ca82ef12df69c10627d` |
| `benchmark/config/primary/benchmark-config-primary-uc3-v0.2.json` | `6d3a09fb938ce537b7054e658220ff84a2276739206bfc0100e27c095bdcaf99` |

Exact manifest path:
`benchmark/config/primary/primary_benchmark_config_freeze_manifest.json`.
The manifest binds the frozen configurations, both schema versions, the prior
decision artifact, generation and retrieval configurations, the task-set plan,
the 30-task freeze manifest, and the specified workflow source files by SHA256.

The execution-order manifest is **not yet frozen**; run order remains pending.
The final benchmark execution code revision is **not yet frozen** because
benchmark orchestration/harness qualification remains pending. This
configuration freeze does not authorize primary benchmark execution.

No primary benchmark task T001–T030 was executed. No result informed this
freeze or any configuration value.

RESULT_DRIVEN_REVISION=NO

BENCHMARK_TASK_EXECUTION=NO

BENCHMARK_STARTED=NO
