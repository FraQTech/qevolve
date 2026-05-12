import numpy as np
from src.program import make_operator, simplify_matrix


def test_make_operator_shape():
    op = make_operator()
    mat = __import__("pennylane").matrix(op)
    assert isinstance(mat, np.ndarray)
    assert mat.shape == (2, 2)


def test_simplify_matrix_identity():
    mat = simplify_matrix()
    assert isinstance(mat, np.ndarray)
    np.testing.assert_allclose(mat, np.eye(2), atol=1e-8)
