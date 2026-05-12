from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicProvider


def make_circuit():
    qc = QuantumCircuit(1, 1)
    qc.x(0)
    qc.measure(0, 0)
    return qc


def run_counts(shots: int = 32):
    qc = make_circuit()
    backend = BasicProvider().get_backend("basic_simulator")
    tqc = transpile(qc, backend)
    result = backend.run(tqc, shots=shots).result()
    return result.get_counts()
