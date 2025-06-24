import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'simulation')))

import numpy as np
from hamiltonian import generate_problem_hamiltonian
from noise_model import noise_hamiltonian
from evolve import simulate_dynamics
from visualize import plot_state_population, plot_overlap, plot_fft

def run_experiment():
    # --- Config ---
    n_qubits = 2
    dim = 2 ** n_qubits
    solution_indices = [1, 3]  # |01⟩ and |11⟩
    timesteps = 150
    delta_t = 0.1
    delta_noise = 0.02

    # --- Initial State: Equal Superposition ---
    psi0 = np.ones(dim, dtype=complex) / np.sqrt(dim)

    # --- Problem Hamiltonian: mark multiple solutions ---
    H_problem = generate_problem_hamiltonian(n_qubits, solution_indices, target_energy=1.0)

    # --- Noise Function ---
    noise_fn = lambda: noise_hamiltonian(n_qubits, delta=delta_noise)

    # --- Simulate Time Evolution ---
    print("Simulating time evolution...")
    states = simulate_dynamics(H_problem, psi0, noise_fn, timesteps, delta_t)

    # --- Visualize Results ---
    for idx in solution_indices:
        plot_state_population(states, target_index=idx)

    overlaps = plot_overlap(states)
    plot_fft(overlaps, delta_t=delta_t)

if __name__ == "__main__":
    run_experiment()
