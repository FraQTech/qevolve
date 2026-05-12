from src.program import gate_label, run_measurements


def test_gate_label():
    assert gate_label() == "my_x_gate"


def test_run_measurements_shape():
    values = run_measurements(8)
    assert isinstance(values, list)
    assert len(values) == 8
    assert set(values).issubset({0, 1})
    assert values == [1] * 8
