import math
from src.program import make_rotation_angle, run_circuit


def test_make_rotation_angle_shape():
    angle = make_rotation_angle()
    assert isinstance(angle, float)
    assert angle > 0.0


def test_run_circuit_value():
    value = run_circuit(0.0)
    assert isinstance(value, float)
    assert math.isclose(value, 1.0, rel_tol=1e-9, abs_tol=1e-9)
