from src.program import make_bell_circuit, run_counts


def test_make_bell_circuit_shape():
    qc = make_bell_circuit()
    assert qc.num_qubits == 2
    assert qc.num_clbits == 2
    assert qc.count_ops().get("h", 0) == 1
    assert qc.count_ops().get("cx", 0) == 1
    assert qc.count_ops().get("measure", 0) == 2


def test_run_counts_shape():
    shots = 64
    counts = run_counts(shots=shots)
    assert isinstance(counts, dict)
    assert counts
    assert set(counts.keys()).issubset({"00", "01", "10", "11"})
    assert sum(counts.values()) == shots
