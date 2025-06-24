import numpy as np
from typing import List

def generate_problem_hamiltonian(n_qubits: int, solution_indices: List[int], target_energy: float = 1.0) -> np.ndarray:
    """
    Generate a diagonal Hamiltonian H ∈ C^{2^n × 2^n} where:
    - solution_indices: indices of basis states that represent solutions
    - target_energy: energy value assigned to solution states
    - all other states have energy 0

    Parameters:
        n_qubits (int): number of qubits
        solution_indices (List[int]): indices of solution basis states
        target_energy (float): energy assigned to each solution index

    Returns:
        H (np.ndarray): Diagonal Hamiltonian matrix
    """
    dim = 2 ** n_qubits
    energies = np.zeros(dim)

    for idx in solution_indices:
        if 0 <= idx < dim:
            energies[idx] = target_energy
        else:
            raise ValueError(f"Index {idx} out of bounds for {n_qubits} qubits.")

    H = np.diag(energies)
    return H
