# Benchmark Notes: qevolve_qiskit_ctrl_0002

- Ecosystem: Qiskit
- Category: quantuminstance_removal
- Source: controlled
- Target version: qiskit 2.3.1
- commit_before: d6f03aeb606a70867ee4e4463ddf3f6e46cc6bf9
- commit_after: 86586db3858bd6bc88af9eb1e0c013f2b0584547

## Failure signal
ImportError: cannot import name 'QuantumInstance' from 'qiskit.utils'

## Gold fix
Replace the removed QuantumInstance-based execution helper with:
- `transpile(circuit, backend)`
- `backend.run(transpiled_circuit, shots=...)`

## Check
`pytest -q`

## Notes
Acceptance checks verify that a 1-qubit measured circuit runs on a simulator-only path and returns count keys in `{"0", "1"}` with total counts equal to the requested shot count.

The passing run may emit a warning that Aer is not installed and BasicSimulator is used instead. This is acceptable for this controlled simulator-only benchmark.