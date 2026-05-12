# Benchmark Notes: qevolve_cirq_ctrl_0012

- Ecosystem: Cirq
- Category: deprecated_helper_protocol_migration
- Source: controlled
- Target version: cirq 1.6.1
- commit_before: <PASTE_FAILING_SHA_HERE>
- commit_after: <PASTE_PASSING_SHA_HERE>

## Failure signal
AttributeError caused by cirq.merge_single_qubit_gates_into_phased_x_z being unavailable.

## Gold fix
Replace:
- cirq.merge_single_qubit_gates_into_phased_x_z(circuit)

with:
- cirq.merge_single_qubit_gates_to_phased_x_and_z(circuit)

## Check
pytest -q

## Notes
Acceptance checks verify that the optimized circuit remains unitary-equivalent to the original tiny 1-qubit circuit and does not increase operation count.
