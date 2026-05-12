from src.program import simple_circuit, run_simple_circuit


def test_simple_circuit_shape():
    qc = simple_circuit()
    assert qc.num_qubits == 1
    assert qc.num_clbits == 1
    assert qc.count_ops().get("measure", 0) == 1


def test_run_simple_circuit_counts():
    shots = 32
    counts = run_simple_circuit(shots=shots)

    assert isinstance(counts, dict)
    assert counts
    assert set(counts.keys()).issubset({"0", "1"})
    assert sum(counts.values()) == shots