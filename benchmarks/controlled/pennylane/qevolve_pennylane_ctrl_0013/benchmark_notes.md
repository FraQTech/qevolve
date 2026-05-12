# Benchmark Notes: qevolve_pennylane_ctrl_0013

- Ecosystem: PennyLane
- Category: legacy_device_name_removal
- Source: controlled
- Target version: pennylane 0.44.1
- commit_before: <PASTE_FAILING_SHA_HERE>
- commit_after: <PASTE_PASSING_SHA_HERE>

## Failure signal
Device construction fails because default.qubit.legacy is no longer supported.

## Gold fix
Replace:
- qml.device("default.qubit.legacy", wires=1)

with:
- qml.device("default.qubit", wires=1)

## Check
pytest -q

## Notes
Acceptance checks verify that a tiny 1-wire QNode still runs on a simulator-only device and returns deterministic probabilities for RY(0.0).
