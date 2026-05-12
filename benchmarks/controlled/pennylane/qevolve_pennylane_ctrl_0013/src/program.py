import pennylane as qml


def make_angle():
    return 0.0


def run_probs(x=None):
    if x is None:
        x = make_angle()

    dev = qml.device("default.qubit", wires=1)

    @qml.qnode(dev)
    def circuit(angle):
        qml.RY(angle, wires=0)
        return qml.probs(wires=0)

    probs = circuit(x)
    return [float(v) for v in probs]
