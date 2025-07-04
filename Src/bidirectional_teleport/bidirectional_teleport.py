# 📡 Bidirectional Quantum Teleportation (BQT)
# Two users (Alice and Bob) simultaneously teleport quantum states to each other

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, execute
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# Create quantum and classical registers
qreg = QuantumRegister(4, name='q')   # q0: Alice's input, q1: Alice's entangled, q2: Bob's entangled, q3: Bob's input
creg = ClassicalRegister(4, name='c') # c0-c1 for Alice's Bell, c2-c3 for Bob's Bell
qc = QuantumCircuit(qreg, creg)

# Prepare arbitrary state for Alice (q0) and Bob (q3)
qc.h(0)
qc.u(0.3, 0.2, 0.1, 0)    # Alice's qubit (q0)
qc.h(3)
qc.u(0.5, 0.4, 0.3, 3)    # Bob's qubit (q3)

# Create entanglement between q1-q2
qc.h(1)
qc.cx(1, 2)

# Alice's Bell Measurement on q0 and q1
qc.cx(0, 1)
qc.h(0)
qc.measure(0, 0)
qc.measure(1, 1)

# Bob's Bell Measurement on q3 and q2
qc.cx(3, 2)
qc.h(3)
qc.measure(3, 2)
qc.measure(2, 3)

# Add classical-controlled gates (in practice done after classical communication)
# These would be applied on Bob's destination qubit (q2) and Alice's (q1) based on measured bits
# In simulation, we must simulate classically to determine final states

# Simulate circuit
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()

print("\n🔁 Bidirectional Quantum Teleportation Result (Measurement Counts):")
print(counts)

# For statevector debugging (optional)
sim_sv = Aer.get_backend('statevector_simulator')
sv_result = execute(qc.remove_final_measurements(inplace=False), sim_sv).result()
sv = sv_result.get_statevector()
print("\n🔬 Statevector (before measurement):")
print(sv)

# Optional: Draw the circuit
qc.draw('mpl')
plt.title("Bidirectional Quantum Teleportation")
plt.tight_layout()
plt.show()
