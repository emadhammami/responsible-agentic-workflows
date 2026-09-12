# Benchmark Tasks

The primary benchmark contains 30 human-validated tasks: 10 for each of
UC1, UC2, and UC3.

Task files must conform to `benchmark/schema/task.schema.json`.

The balanced allocation per use case is:

- 3 direct retrieval tasks;
- 3 within-document reasoning tasks;
- 2 cross-document reasoning tasks;
- 2 insufficient-evidence tasks.

Conflicting-document reasoning remains supported by the task schema but is not
a required category in the balanced primary benchmark.

Questions should represent realistic document-based knowledge work rather than
simple document-title or legal-reference lookup.

Reference answers and reference evidence must be human-verified before a task
is frozen. They must never be made available to B0, B1, or G1 during runtime.

A task must not be added, removed, rewritten, or reclassified because of
observed benchmark performance.
