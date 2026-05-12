# Benchmark Notes: qevolve_qiskit_ctrl_0007

- Ecosystem: Qiskit
- Category: import_path_rename
- Source: controlled
- Target version: qiskit 2.3.1
- commit_before: <PASTE_FAILING_SHA_HERE>
- commit_after: <PASTE_PASSING_SHA_HERE>

## Failure signal
Import failure caused by rom qiskit.tools import parallel_map.

## Gold fix
Replace:
- rom qiskit.tools import parallel_map

with:
- rom qiskit.utils import parallel_map

## Check
pytest -q

## Notes
Acceptance checks verify that the helper still computes the expected squared values on a tiny deterministic input list after the import-path migration.
