import pennylane as qml
from pennylane.tape import QuantumScript


def make_angle():
    return 0.0


def make_tape(x=None):
    if x is None:
        x = make_angle()

    ops = [qml.RX(x, wires=0)]
    measurements = [qml.expval(qml.PauliZ(0))]
    return QuantumScript(ops, measurements)


def run_execute(x=None):
    tape = make_tape(x)
    dev = qml.device("default.qubit", wires=1)
    results = qml.execute([tape], dev)
    return float(results[0])
