# Controlled Quantum Teleportation (CQT) – Executable Program (GHZ based)

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Define the Controlled Quantum Teleportation Circuit (GHZ based)
def controlled_quantum_teleportation(alpha=1/2, beta=(3**0.5)/2):
    qr = QuantumRegister(4, 'q')  # q0: Alice's qubit, q1: entangled with Alice, q2: Charlie, q3: Bob
    cr = ClassicalRegister(3, 'c')  # c0, c1: Alice's measurement; c2: Charlie's measurement
    circuit = QuantumCircuit(qr, cr)

    # Step 1: Initialize Alice's state
    circuit.initialize([alpha, beta], 0)

    # Step 2: GHZ state creation among q1 (Alice), q2 (Charlie), q3 (Bob)
    circuit.h(1)
    circuit.cx(1, 2)
    circuit.cx(2, 3)

    # Step 3: Bell measurement by Alice (q0 and q1)
    circuit.cx(0, 1)
    circuit.h(0)
    circuit.measure(0, 0)
    circuit.measure(1, 1)

    # Step 4: Charlie's measurement (q2)
    circuit.measure(2, 2)

    # Step 5: Conditional Pauli corrections on Bob's qubit q3
    # Define classical logic gates (example shown for demo)
    # These conditions should cover all 8 combinations of 3 classical bits (000 to 111)
    circuit.x(3).c_if(cr, 0b001)  # if Charlie=1 only (permissive logic)
    circuit.z(3).c_if(cr, 0b010)
    circuit.x(3).c_if(cr, 0b011)
    circuit.z(3).c_if(cr, 0b100)
    circuit.x(3).c_if(cr, 0b101)
    circuit.z(3).c_if(cr, 0b110)
    circuit.x(3).c_if(cr, 0b111)

    return circuit

# Simulate the circuit
def simulate_cqt():
    circuit = controlled_quantum_teleportation()
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend=backend, shots=1024)
    result = job.result()
    counts = result.get_counts()
    print("Measurement Results:", counts)
    plot_histogram(counts)
    plt.title("Controlled Quantum Teleportation (GHZ)")
    plt.show()

if __name__ == '__main__':
    simulate_cqt()
