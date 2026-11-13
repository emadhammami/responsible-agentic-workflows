# Resource-boundary substudy — constrained four-call mechanism

**Status:** Public derived companion data. Separate from Study B's main 144 executions.

Six distinct families, two policies, three repetitions: 36 execution records and 18 matched pairs. The 36 published validation rows record `resource_stopped`. The original study reports zero released completed tasks for either policy. G1 used 27,520 tokens versus 39,697 for B1 (a 30.67% reduction), with 18 reported reservation-gate events. B1's 18 supported intermediate revisions were **not released completed outcomes**.

## Included files

- `data/execution_integrity.csv`: recorded integrity flags, status and native-record hashes for all 36 runs; does not contain native records.
- `data/reported_metrics.json`: transcribed source aggregates and source checksums.
- `reproduce.py`: validates the released rows and recomputes the percentage from **reported** token totals.

From the repository root: `python research-artifacts/resource-boundary/reproduce.py --output /tmp/usn-boundary-reconstructed`

**Inference boundary:** Saving tokens when a recovery cannot be finished is not improved task completion. These runs must not be combined with Study B's main 144-run denominator. The original underlying model calls and reservation events are not independently reconstructed by this companion package.
