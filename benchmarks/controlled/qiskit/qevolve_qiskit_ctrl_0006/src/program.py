from qiskit import QuantumCircuit, transpile
from qiskit.providers.fake_provider import GenericBackendV2


def make_bell_circuit():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc


def run_counts(shots: int = 64):
    qc = make_bell_circuit()
    backend = GenericBackendV2(num_qubits=2)
    tqc = transpile(qc, backend)
    result = backend.run(tqc, shots=shots).result()
    return result.get_counts()
