import math
from src.program import make_angle, make_tape, run_execute


def test_make_angle_shape():
    angle = make_angle()
    assert isinstance(angle, float)


def test_make_tape_shape():
    tape = make_tape(0.0)
    assert len(tape.operations) == 1
    assert len(tape.measurements) == 1
    assert tape.operations[0].name == "RX"


def test_run_execute_value():
    value = run_execute(0.0)
    assert isinstance(value, float)
    assert math.isclose(value, 1.0, rel_tol=1e-9, abs_tol=1e-9)
