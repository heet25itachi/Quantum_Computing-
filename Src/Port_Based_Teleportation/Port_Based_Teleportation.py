# Port-Based Quantum Teleportation (PBT)
# Author: Heet Trivedi (aka Arjun)
# Description: A Qiskit-based simulation of Port-Based Teleportation with fidelity measurement

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, execute
from qiskit.quantum_info import Statevector, partial_trace, state_fidelity
import numpy as np

# === Parameters ===
n_ports = 4  # Number of ports (entangled Bell pairs)
shots = 1024

# === Helper: Create Bell pair ===
def create_bell_pair(qc, q0, q1):
    qc.h(q0)
    qc.cx(q0, q1)

# === Step 1: Prepare Port-Based Resource State ===
def prepare_pbt_resource(qc, alice_q, bob_q):
    for i in range(n_ports):
        create_bell_pair(qc, alice_q[i], bob_q[i])

# === Step 2: Prepare Input State to Teleport ===
def prepare_input_state(qc, psi_q):
    qc.h(psi_q)    # Example: |+⟩ state
    qc.t(psi_q)

# === Step 3: Alice's Generalized Measurement (Simulated POVM Placeholder) ===
def simulate_pbt_measurement():
    # Simulated: randomly select a port (in real case: POVM)
    return np.random.randint(0, n_ports)

# === Step 4: Simulate the Full Protocol ===
def port_based_teleport():
    psi = QuantumRegister(1, 'psi')
    alice = QuantumRegister(n_ports, 'alice')
    bob = QuantumRegister(n_ports, 'bob')
    cr = ClassicalRegister(1, 'c')
    qc = QuantumCircuit(psi, alice, bob, cr)

    prepare_input_state(qc, psi[0])
    prepare_pbt_resource(qc, alice, bob)

    # Placeholder: Assume Alice measures and port_index is where the state lands
    port_index = simulate_pbt_measurement()

    # Trace out everything except Bob's selected port and compare fidelity
    backend = Aer.get_backend('statevector_simulator')
    result = execute(qc, backend).result()
    final_state = Statevector(result.get_statevector(qc))

    bob_ports = [bob[i] for i in range(n_ports)]
    traced = partial_trace(final_state, [q for q in final_state._dims.keys() if q != bob_ports[port_index]])

    # Reference: Ideal teleported state |+⟩ after H + T gate
    ref_qc = QuantumCircuit(1)
    ref_qc.h(0)
    ref_qc.t(0)
    ref_sv = Statevector.from_instruction(ref_qc)

    fidelity = state_fidelity(ref_sv, traced)
    print(f"[PBT] Selected port: {port_index} | Fidelity with ideal state: {fidelity:.4f}")

if __name__ == "__main__":
    port_based_teleport()
