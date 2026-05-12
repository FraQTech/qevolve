# Benchmark Notes: qevolve_cirq_ctrl_0010

- Ecosystem: Cirq
- Category: deprecated_base_class_migration
- Source: controlled
- Target version: cirq 1.6.1
- commit_before: <PASTE_FAILING_SHA_HERE>
- commit_after: <PASTE_PASSING_SHA_HERE>

## Failure signal
AttributeError caused by cirq.SingleQubitGate being unavailable.

## Gold fix
Replace a custom gate definition based on:
- class MyXGate(cirq.SingleQubitGate)

with a modern Cirq gate definition based on:
- class MyXGate(cirq.Gate)
- _num_qubits_(self) -> 1
- _unitary_(self)

## Check
pytest -q

## Notes
Acceptance checks verify that a tiny 1-qubit custom gate circuit runs on the default simulator and deterministically measures all ones after an X-like gate followed by measurement.
