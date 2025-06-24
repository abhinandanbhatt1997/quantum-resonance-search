import numpy as np
from typing import Callable

def sample_epsilon(delta: float = 0.01) -> float:
    """
    Sample a small random noise amplitude from a normal distribution.
    
    Parameters:
        delta (float): standard deviation of the noise
        
    Returns:
        epsilon (float): sampled noise value
    """
    return np.random.normal(loc=0.0, scale=delta)

def build_sigma_x_sum(n_qubits: int) -> np.ndarray:
    """
    Build the operator sum_j σ_x^j for n qubits as a matrix.

    Returns:
        Sx_sum (np.ndarray): Hamiltonian term with σ_x acting on each qubit
    """
    I = np.eye(2)
    X = np.array([[0, 1], [1, 0]])
    dim = 2 ** n_qubits
    Sx_sum = np.zeros((dim, dim), dtype=complex)

    for j in range(n_qubits):
        ops = [I] * n_qubits
        ops[j] = X
        term = ops[0]
        for op in ops[1:]:
            term = np.kron(term, op)
        Sx_sum += term

    return Sx_sum

def noise_hamiltonian(n_qubits: int, delta: float = 0.01) -> np.ndarray:
    """
    Generate a single-shot noise Hamiltonian H_noise(t) = ε(t) * Σ σ_x^j.

    Parameters:
        n_qubits (int): number of qubits
        delta (float): std deviation of noise

    Returns:
        H_noise (np.ndarray): time-dependent noise Hamiltonian
    """
    epsilon_t = sample_epsilon(delta)
    Sx_sum = build_sigma_x_sum(n_qubits)
    return epsilon_t * Sx_sum
