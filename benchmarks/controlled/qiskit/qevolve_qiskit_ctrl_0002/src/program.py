from qiskit import QuantumCircuit, transpile
from qiskit.providers.fake_provider import GenericBackendV2


def simple_circuit():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    return qc


def run_simple_circuit(shots: int = 32):
    backend = GenericBackendV2(
        num_qubits=1,
        basis_gates=["id", "rz", "sx", "x"],
        seed=42,
    )
    qc = simple_circuit()
    tqc = transpile(qc, backend)
    job = backend.run(tqc, shots=shots)
    result = job.result()
    return result.get_counts()