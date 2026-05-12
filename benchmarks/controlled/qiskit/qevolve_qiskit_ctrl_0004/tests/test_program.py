from src.program import make_circuit, export_qasm


def test_make_circuit_shape():
    qc = make_circuit()
    assert qc.num_qubits == 1
    assert qc.num_clbits == 1
    assert qc.count_ops().get("h", 0) == 1
    assert qc.count_ops().get("measure", 0) == 1


def test_export_qasm_text_shape():
    text = export_qasm()
    assert isinstance(text, str)
    assert "OPENQASM" in text
    assert 'include "qelib1.inc"' in text
    assert "qreg q[1];" in text
    assert "creg c[1];" in text
    assert "h q[0];" in text
    assert "measure q[0] -> c[0];" in text
