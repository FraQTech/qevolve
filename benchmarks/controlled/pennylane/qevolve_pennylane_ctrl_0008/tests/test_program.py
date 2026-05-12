from src.program import make_script, export_qasm


def test_make_script_shape():
    script = make_script()
    assert len(script.operations) == 2
    assert len(script.measurements) == 1
    assert script.operations[0].name == "Hadamard"
    assert script.operations[1].name == "CNOT"


def test_export_qasm_text_shape():
    text = export_qasm()
    assert isinstance(text, str)
    assert "OPENQASM 2.0;" in text
    assert 'include "qelib1.inc";' in text
    assert "qreg q[2];" in text
    assert "creg c[2];" in text
    assert "h q[0];" in text
    assert ("cx q[0],q[1];" in text) or ("cx q[0], q[1];" in text)
