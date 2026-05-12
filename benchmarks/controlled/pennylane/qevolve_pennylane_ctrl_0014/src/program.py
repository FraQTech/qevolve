import pennylane as qml
import numpy as np


def make_operator():
    return qml.X(0) @ qml.X(0)


def simplify_matrix():
    op = make_operator()
    simplified = qml.simplify(op)
    return qml.matrix(simplified)
