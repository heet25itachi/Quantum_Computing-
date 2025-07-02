#Quantum Teleportation Protocol - Using Qiksit
#Author: Arjun Trivedi 

from qiksit import QUnatumCircuit, Aer, execute
from qiksit.visualization import plot_histogram 
import matplotlib.pyplot as plt 

#Step 1: Create a Quantum Circuit with 3 qubits and 3 classical bits 
qc = QuantumCircuit(3,3)

#Step 2: Prepare the state to teleport (say qubit 0 in |+>state)
qc.h(0) # Create superposition on qubit 0

#Step 3: Create an entangled pair between qubits 1 and qubit 2 
qc.h(1)
qc.cx(1,2)

#Step 4: Bell measurement on qubit 0 and qubit 1 
qc.cx(0,1)
qc.h(0)
qc.barrier()
qc.measure([0,1],[0,1])    # Measure qubit 0 and 1 into classical bits 0 and 1

#Step 5: Apply conditional opertaions on qubit 2 based on measurements 
qc.cx(1,2)
qc.cx(0,2)
qc.measure(2,2)   # Final measurement of teleport qubit

#Step 6: Simulate the circuit using QASM simulator = Aer.get_backend('qasm_simulator')
job = execute(qc,backend=simulator,shots = 1024)
result = job.result()
counts = result.get_counts()

#Step 7: Visualize the results
print("Quantum Teleportation Meausurement Results:")
print(counts)
plot_histogram(counts)
plt.show()
