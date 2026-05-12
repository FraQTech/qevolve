from qiskit.utils import parallel_map


def square(x: int) -> int:
    return x * x


def compute_squares(values):
    return parallel_map(square, values)
