from qiskit import QuantumCircuit
from qiskit.qasm2 import dumps


def make_circuit():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    return qc


def export_qasm():
    qc = make_circuit()
    return dumps(qc)
