import numpy as np
from scipy.linalg import expm
from typing import Callable, List

def simulate_dynamics(
    H_problem: np.ndarray,
    psi0: np.ndarray,
    noise_fn: Callable[[], np.ndarray],
    timesteps: int,
    delta_t: float = 0.1
) -> List[np.ndarray]:
    """
    Simulate time evolution under H(t) = H_problem + H_noise(t)
    
    Parameters:
        H_problem (np.ndarray): static diagonal Hamiltonian
        psi0 (np.ndarray): initial state vector
        noise_fn (Callable): function that returns H_noise(t)
        timesteps (int): number of steps to simulate
        delta_t (float): time step size

    Returns:
        List of evolved state vectors at each time step
    """
    psi = psi0.copy()
    states = [psi0.copy()]
    
    for t in range(timesteps):
        H_noise_t = noise_fn()
        H_total = H_problem + H_noise_t
        U = expm(-1j * H_total * delta_t)
        psi = U @ psi
        states.append(psi.copy())
    
    return states
