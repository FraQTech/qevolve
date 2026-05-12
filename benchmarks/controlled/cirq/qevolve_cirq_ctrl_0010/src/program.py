import cirq
import numpy as np


def gate_label():
    return "my_x_gate"


def run_measurements(repetitions: int = 8):
    q = cirq.LineQubit(0)

    class MyXGate(cirq.Gate):
        def _num_qubits_(self):
            return 1

        def _unitary_(self):
            return np.array([[0, 1], [1, 0]])

        def __str__(self):
            return "MX"

    circuit = cirq.Circuit(
        MyXGate().on(q),
        cirq.measure(q, key="m"),
    )

    result = cirq.Simulator().run(circuit, repetitions=repetitions)
    return result.measurements["m"].flatten().tolist()
