import numpy as np
import matplotlib.pyplot as plt
from typing import List

def plot_state_population(states: List[np.ndarray], target_index: int):
    """
    Plot population |⟨target|ψ(t)⟩|^2 over time.

    Parameters:
        states (List[np.ndarray]): List of state vectors
        target_index (int): Basis index of the target state
    """
    probs = [abs(state[target_index])**2 for state in states]
    plt.figure(figsize=(8, 4))
    plt.plot(probs, label=f'P[{target_index}]')
    plt.xlabel("Time step")
    plt.ylabel("Population")
    plt.title("Target State Population Over Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_overlap(states: List[np.ndarray]):
    """
    Plot overlap C(t) = ⟨ψ(0)|ψ(t)⟩ over time.

    Parameters:
        states (List[np.ndarray]): List of state vectors
    """
    psi0 = states[0]
    overlaps = [np.vdot(psi0, psi_t) for psi_t in states]
    overlaps_magnitude = [abs(c)**2 for c in overlaps]

    plt.figure(figsize=(8, 4))
    plt.plot(overlaps_magnitude, label="|⟨ψ(0)|ψ(t)⟩|^2")
    plt.xlabel("Time step")
    plt.ylabel("Overlap")
    plt.title("Overlap with Initial State")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    return overlaps


def plot_fft(overlap_series: List[complex], delta_t: float = 0.1):
    """
    Plot FFT of the overlap ⟨ψ(0)|ψ(t)⟩ to detect resonance frequencies.

    Parameters:
        overlap_series (List[complex]): list of overlaps ⟨ψ(0)|ψ(t)⟩
        delta_t (float): time step used in simulation
    """
    overlaps = np.array(overlap_series)
    fft_vals = np.fft.fft(overlaps)
    freqs = np.fft.fftfreq(len(overlaps), d=delta_t)

    plt.figure(figsize=(8, 4))
    plt.plot(freqs, np.abs(fft_vals), label="FFT")
    plt.xlabel("Frequency")
    plt.ylabel("Amplitude")
    plt.title("Fourier Transform of Overlap")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
