import pennylane as qml
from pennylane.tape import QuantumScript


def make_script():
    ops = [
        qml.Hadamard(wires=0),
        qml.CNOT(wires=[0, 1]),
    ]
    measurements = [qml.probs(wires=[0, 1])]
    return QuantumScript(ops, measurements)


def export_qasm():
    script = make_script()
    return qml.to_openqasm(script)
