from src.program import make_parameterized_circuit, bind_value


def test_make_parameterized_circuit():
    qc, theta = make_parameterized_circuit()
    assert qc.num_qubits == 1
    assert len(qc.parameters) == 1
    assert theta in qc.parameters


def test_bind_value_removes_free_parameter():
    bound = bind_value(0.5)
    assert bound.num_qubits == 1
    assert len(bound.parameters) == 0
    assert bound.count_ops().get("ry", 0) == 1