from qiskit import QuantumCircuit, transpile
from qiskit.providers.fake_provider import GenericBackendV2


def bell_counts(shots: int = 64):
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])

    backend = GenericBackendV2(num_qubits=2)
    transpiled = transpile(qc, backend)
    job = backend.run(transpiled, shots=shots)
    result = job.result()
    return result.get_counts()