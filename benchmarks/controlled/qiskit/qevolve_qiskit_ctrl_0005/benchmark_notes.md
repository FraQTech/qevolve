# Benchmark Notes: qevolve_qiskit_ctrl_0005

- Ecosystem: Qiskit
- Category: backend_provider_namespace_drift
- Source: controlled
- Target version: qiskit 2.3.1
- commit_before: <failing_commit_sha>
- commit_after: <passing_commit_sha>

## Failure signal
ImportError caused by `from qiskit import BasicAer` no longer being supported.

## Gold fix
Replace:
- `from qiskit import BasicAer`
- `BasicAer.get_backend("qasm_simulator")`

with:
- `from qiskit.providers.basic_provider import BasicProvider`
- `BasicProvider().get_backend("basic_simulator")`

## Check
`pytest -q`

## Notes
Acceptance checks verify that a tiny measured circuit still runs on a simulator-only backend and returns a count dictionary with total shots preserved.