# Benchmark Notes: qevolve_pennylane_ctrl_0011

- Ecosystem: PennyLane
- Category: execution_keyword_removal
- Source: controlled
- Target version: pennylane 0.44.1
- commit_before: <PASTE_FAILING_SHA_HERE>
- commit_after: <PASTE_PASSING_SHA_HERE>

## Failure signal
TypeError caused by passing the removed max_expansion keyword to qml.execute.

## Gold fix
Replace:
- qml.execute([tape], dev, max_expansion=10)

with:
- qml.execute([tape], dev)

## Check
pytest -q

## Notes
Acceptance checks verify that a tiny 1-wire QuantumScript still executes on default.qubit and returns the expected deterministic expval for RX(0.0).
