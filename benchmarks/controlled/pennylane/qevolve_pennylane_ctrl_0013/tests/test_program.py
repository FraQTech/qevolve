import math
from src.program import make_angle, run_probs


def test_make_angle_shape():
    angle = make_angle()
    assert isinstance(angle, float)


def test_run_probs_value():
    probs = run_probs(0.0)
    assert isinstance(probs, list)
    assert len(probs) == 2
    assert math.isclose(probs[0], 1.0, rel_tol=1e-9, abs_tol=1e-9)
    assert math.isclose(probs[1], 0.0, rel_tol=1e-9, abs_tol=1e-9)
