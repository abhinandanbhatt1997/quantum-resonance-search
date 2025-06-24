import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'simulation')))

import numpy as np
from hamiltonian import generate_problem_hamiltonian
from noise_model import noise_hamiltonian
from evolve import simulate_dynamics
from visualize import plot_state_population, plot_overlap, plot_fft

def run_experiment():
    n_qubits = 10
    dim = 2 ** n_qubits
    solution_index = 777  # Arbitrary marked state
    timesteps = 120
    delta_t = 0.05
    delta_noise = 0.01  # Go a bit lower due to high dimension

    # --- Initial equal superposition ---
    psi0 = np.ones(dim, dtype=complex) / np.sqrt(dim)

    print("Building 10-qubit problem Hamiltonian...")
    H_problem = generate_problem_hamiltonian(n_qubits, [solution_index], target_energy=1.0)
    noise_fn = lambda: noise_hamiltonian(n_qubits, delta=delta_noise)

    print("Evolving quantum system...")
    states = simulate_dynamics(H_problem, psi0, noise_fn, timesteps, delta_t)

    plot_state_population(states, target_index=solution_index)
    overlaps = plot_overlap(states)
    plot_fft(overlaps, delta_t=delta_t)

if __name__ == "__main__":
    run_experiment()
