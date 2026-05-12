from src.program import make_circuit, run_counts


def test_make_circuit_shape():
    qc = make_circuit()
    assert qc.num_qubits == 1
    assert qc.num_clbits == 1
    assert qc.count_ops().get("x", 0) == 1
    assert qc.count_ops().get("measure", 0) == 1


def test_run_counts_shape():
    shots = 32
    counts = run_counts(shots=shots)
    assert isinstance(counts, dict)
    assert counts
    assert set(counts.keys()).issubset({"0", "1"})
    assert sum(counts.values()) == shots
