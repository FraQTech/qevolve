# Benchmark Notes: qevolve_qiskit_ctrl_0004

- Ecosystem: Qiskit
- Category: circuit_export_migration
- Source: controlled
- Target version: qiskit 2.3.1
- commit_before: 80c4f77ef1bd9ca1ae7b5894271ee03937b9fe8d
- commit_after: 3da73a32cfde6fb9351ba136d617221e6f291115

## Failure signal
AttributeError: 'QuantumCircuit' object has no attribute 'qasm'

## Gold fix
Replace:
- `qc.qasm()`

with:
- `qiskit.qasm2.dumps(qc)`

## Check
`pytest -q`

## Notes
Acceptance checks verify that a tiny measured circuit exports to OpenQASM text containing the expected header, register declarations, and gate/measurement statements.