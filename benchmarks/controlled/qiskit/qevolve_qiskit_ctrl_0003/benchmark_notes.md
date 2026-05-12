# Benchmark Notes: qevolve_qiskit_ctrl_0003

- Ecosystem: Qiskit
- Category: parameter_binding_migration
- Source: controlled
- Target version: qiskit 2.3.1
- commit_before: ed7090a7d265af69022cd809a7ed45dae11f4915
- commit_after: 5a85d809c3232eae69573376249716ce89c5c060

## Failure signal
AttributeError: 'QuantumCircuit' object has no attribute 'bind_parameters'

## Gold fix
Replace:
- `bind_parameters({...})`

with:
- `assign_parameters({...})`

## Check
`pytest -q`

## Notes
Acceptance checks verify that a parameterized 1-qubit circuit is created correctly and that binding a numeric value removes the free parameter while preserving the `ry` operation.