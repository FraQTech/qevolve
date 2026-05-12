from qiskit.circuit import QuantumCircuit, Parameter


def make_parameterized_circuit():
    theta = Parameter("theta")
    qc = QuantumCircuit(1)
    qc.ry(theta, 0)
    return qc, theta


def bind_value(value: float):
    qc, theta = make_parameterized_circuit()
    bound = qc.assign_parameters({theta: value})
    return bound