# Controlled Quantum Teleportation (CQT) using GHZ and Cluster states
# Author: Heet Trivedi

try:
    from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, Aer, execute
    from qiskit.visualization import plot_histogram
    from qiskit.quantum_info import Statevector
    import matplotlib.pyplot as plt
    import numpy as np
    qiskit_available = True
except ImportError:
    print("Qiskit not available in this environment. Simulation and plotting disabled.")
    qiskit_available = False

if qiskit_available:

    def controlled_teleportation_ghz(alpha, beta):
        q = QuantumRegister(4, 'q')
        c = ClassicalRegister(3, 'c')
        circuit = QuantumCircuit(q, c)

        circuit.initialize([alpha, beta], 0)

        circuit.h(1)
        circuit.cx(1, 2)
        circuit.cx(2, 3)

        circuit.cx(0, 1)
        circuit.h(0)
        circuit.measure(0, 0)
        circuit.measure(1, 1)

        circuit.measure(2, 2)

        return circuit

    def controlled_teleportation_cluster(alpha, beta):
        q = QuantumRegister(4, 'q')
        c = ClassicalRegister(3, 'c')
        circuit = QuantumCircuit(q, c)

        circuit.initialize([alpha, beta], 0)

        circuit.h(1)
        circuit.h(2)
        circuit.h(3)
        circuit.cz(1, 2)
        circuit.cz(2, 3)

        circuit.cx(0, 1)
        circuit.h(0)
        circuit.measure(0, 0)
        circuit.measure(1, 1)

        circuit.measure(2, 2)

        return circuit

    def simulate_and_plot(circuit, title):
        backend = Aer.get_backend('qasm_simulator')
        result = execute(circuit, backend=backend, shots=1024).result()
        counts = result.get_counts()
        print(f"\n🔍 Results for {title}:")
        print(counts)
        plot_histogram(counts, title=title)
        plt.show()

    alpha = 1/np.sqrt(3)
    beta = np.sqrt(2/3)

    circuit_ghz = controlled_teleportation_ghz(alpha, beta)
    simulate_and_plot(circuit_ghz, "Controlled Teleportation - GHZ State")

    circuit_cluster = controlled_teleportation_cluster(alpha, beta)
    simulate_and_plot(circuit_cluster, "Controlled Teleportation - Cluster State")

else:
    print("Skipping simulation due to missing Qiskit environment.")
