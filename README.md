Quantum Resonance Search (QRS)

Oracle-free, noise-powered quantum search via resonant dynamics.

Quantum Resonance Search (QRS) is a novel quantum computing framework that discovers hidden solution states by using controlled noise to induce resonance in quantum systems. Unlike Grover’s algorithm, QRS doesn’t require oracles or deep quantum circuits. Instead, it exploits natural Hamiltonian dynamics and decoherence to amplify solutions and detect them via Fourier analysis of system evolution.

🌟 Key Concepts
🎯 Solution as Eigenstate: Target solutions are encoded as eigenstates in a Hamiltonian.

🌪️ Noise Injection: Low-amplitude white or log-swept noise perturbs the system, causing resonant states to amplify.

🧠 No Oracle: Solutions emerge from the physics of evolution, not black-box queries.

🔍 FFT Detection: Solutions are revealed as frequency peaks in time-domain evolution.

📂 Project Structure
bash
Copy
Edit
quantum-resonance-search/
├── simulation/                # Core simulation engine
│   ├── hamiltonian.py        # Problem Hamiltonian generator
│   ├── noise_model.py        # Noise models: white, log-sweep, etc.
│   ├── evolve.py             # Time evolution simulation
│   ├── visualize.py          # Plotting & analysis utilities
│
├── experiments/              # Configurable experiments
│   ├── exp1_single_solution.py
│   ├── exp2_two_solutions.py
│   ├── exp3_three_qubit_one_solution.py
│   ├── exp4_log_sweep.py     # 🚧 In progress: log-frequency sweep
│
├── results/                  # Generated plots (optional)
└── README.md                 # You're here
🚀 How It Works
Define a problem as a diagonal Hamiltonian:
H = diag(0, 0, 1, 0) → index 2 is the marked state.

Initialize the system in equal superposition.

Inject weak noise into the evolution (white or structured).

Simulate the system’s time evolution using Schrödinger dynamics.

Analyze the system:

Plot population of target states over time

Plot overlap with initial state

Compute FFT to detect resonant frequencies

📈 Sample Output

State 6 shows resonant amplification.


FFT reveals a dominant resonance frequency tied to the target state energy gap.

🔧 Requirements
Python 3.7+

Qiskit or PennyLane (planned support)

numpy, matplotlib, scipy

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run an experiment:

bash
Copy
Edit
python experiments/exp1_single_solution.py
🧪 Applications
Oracle-free quantum search

Energy landscape mapping

Quantum spectroscopy

Noise-assisted quantum computing (NISQ)

Bio-inspired quantum systems

Quantum anomaly detection

📚 References & Inspirations
Grover’s Search

Quantum Stochastic Resonance

Noise-assisted transport in photosynthesis

Quantum Control and Spectroscopy

🤝 Contribute
Got ideas for:

Real hardware runs (e.g., IBM Q)?

Scaling beyond 10 qubits?

Non-diagonal Hamiltonians?

Pull requests, issues, and feedback welcome!

📜 License
MIT License — free to use, modify, share.

