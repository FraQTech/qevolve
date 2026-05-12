# Benchmark Notes: qevolve_pennylane_ctrl_0008

- Ecosystem: PennyLane
- Category: openqasm_export_helper_migration
- Source: controlled
- Target version: pennylane 0.44.1
- commit_before: <PASTE_FAILING_SHA_HERE>
- commit_after: <PASTE_PASSING_SHA_HERE>

## Failure signal
AttributeError caused by QuantumScript.to_openqasm() being unavailable.

## Gold fix
Replace:
- script.to_openqasm()

with:
- qml.to_openqasm(script)

## Check
pytest -q

## Notes
Acceptance checks verify that a tiny 2-wire PennyLane quantum script exports to OpenQASM text containing the expected header, include statement, register declarations, and core gate lines.
