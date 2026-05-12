import cirq
import numpy as np
from src.program import make_circuit, optimize_circuit, final_state


def test_make_circuit_shape():
    circuit = make_circuit()
    ops = list(circuit.all_operations())
    assert len(ops) == 3


def test_optimize_circuit_equivalence():
    original = make_circuit()
    optimized = optimize_circuit()

    assert len(list(optimized.all_operations())) <= len(list(original.all_operations()))

    q_original = sorted(original.all_qubits())
    q_optimized = sorted(optimized.all_qubits())

    original_state = cirq.final_state_vector(original, qubit_order=q_original)
    optimized_state = cirq.final_state_vector(optimized, qubit_order=q_optimized)

    cirq.testing.assert_allclose_up_to_global_phase(
        original_state,
        optimized_state,
        atol=1e-8,
    )


def test_final_state_shape():
    state = final_state()
    assert isinstance(state, np.ndarray)
    assert state.shape == (2,)