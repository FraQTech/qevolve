from src.program import bell_counts


def test_bell_counts_runs():
    counts = bell_counts(64)
    assert isinstance(counts, dict)
    assert sum(counts.values()) == 64