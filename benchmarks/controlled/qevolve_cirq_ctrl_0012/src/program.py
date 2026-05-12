import cirq
import numpy as np


def make_circuit():
    q = cirq.LineQubit(0)
    return cirq.Circuit(
        cirq.H(q),
        cirq.Z(q),
        cirq.S(q),
    )


def optimize_circuit():
    circuit = make_circuit()
    return cirq.merge_single_qubit_gates_to_phased_x_and_z(circuit)


def final_state():
    circuit = optimize_circuit()
    qubits = sorted(circuit.all_qubits())
    return cirq.final_state_vector(circuit, qubit_order=qubits)
