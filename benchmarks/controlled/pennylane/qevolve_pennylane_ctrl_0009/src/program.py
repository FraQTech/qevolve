import pennylane as qml


def make_rotation_angle():
    return 0.123


def run_circuit(x=None):
    if x is None:
        x = make_rotation_angle()

    dev = qml.device("default.qubit", wires=1)

    @qml.qnode(dev)
    def circuit(angle):
        qml.RX(angle, wires=0)
        return qml.expval(qml.PauliZ(0))

    return float(circuit(x))
