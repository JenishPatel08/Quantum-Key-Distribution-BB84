# BB84 with Eve + Visualization (QBER and Key Agreement Rate)

import random
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, execute

def generate_bits_bases(n):
    bits = [random.randint(0, 1) for _ in range(n)]
    bases = [random.choice(['Z', 'X']) for _ in range(n)]
    return bits, bases

def prepare_qubits(bits, bases):
    circuits = []
    for bit, basis in zip(bits, bases):
        qc = QuantumCircuit(1, 1)
        if bit == 1:
            qc.x(0)
        if basis == 'X':
            qc.h(0)
        circuits.append(qc)
    return circuits

def eve_intercept(circuits):
    eve_bases = [random.choice(['Z', 'X']) for _ in circuits]
    intercepted_circuits = []
    for qc, basis in zip(circuits, eve_bases):
        qc_copy = qc.copy()
        if basis == 'X':
            qc_copy.h(0)
        qc_copy.measure(0, 0)
        backend = Aer.get_backend('qasm_simulator')
        job = execute(qc_copy, backend, shots=1)
        result = job.result()
        bit = int(list(result.get_counts().keys())[0])

        new_qc = QuantumCircuit(1, 1)
        if bit == 1:
            new_qc.x(0)
        if basis == 'X':
            new_qc.h(0)
        intercepted_circuits.append(new_qc)
    return intercepted_circuits, eve_bases

def bob_measure(circuits, bob_bases):
    results = []
    for qc, basis in zip(circuits, bob_bases):
        qc_copy = qc.copy()
        if basis == 'X':
            qc_copy.h(0)
        qc_copy.measure(0, 0)
        backend = Aer.get_backend('qasm_simulator')
        job = execute(qc_copy, backend, shots=1)
        result = job.result()
        bit = int(list(result.get_counts().keys())[0])
        results.append(bit)
    return results

def sift_keys(alice_bases, bob_bases, alice_bits, bob_bits):
    sifted_alice, sifted_bob = [], []
    match_positions = []
    for i, (ab, bb) in enumerate(zip(alice_bases, bob_bases)):
        if ab == bb:
            sifted_alice.append(alice_bits[i])
            sifted_bob.append(bob_bits[i])
            match_positions.append(i)
    return sifted_alice, sifted_bob, match_positions

def calculate_qber(key1, key2):
    if not key1:
        return 0
    errors = sum([1 for a, b in zip(key1, key2) if a != b])
    return errors / len(key1)

# Simulation parameters
n = 100

# Step 1: Generate Alice's bits and bases
alice_bits, alice_bases = generate_bits_bases(n)

# Step 2: Prepare qubits
qubits = prepare_qubits(alice_bits, alice_bases)

# Step 3: Eve intercepts
intercepted_qubits, eve_bases = eve_intercept(qubits)

# Step 4: Bob measures
bob_bases = [random.choice(['Z', 'X']) for _ in range(n)]
bob_results = bob_measure(intercepted_qubits, bob_bases)

# Step 5: Sift keys where Alice and Bob used same basis
alice_key, bob_key, match_positions = sift_keys(alice_bases, bob_bases, alice_bits, bob_results)

# Step 6: Calculate QBER
qber = calculate_qber(alice_key, bob_key)
match_rate = len(alice_key) / n

# Step 7: Visualize
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Basis match rate chart
ax[0].bar(["Matched Bases", "Mismatched Bases"], [len(match_positions), n - len(match_positions)], color=["green", "red"])
ax[0].set_title("Basis Matching")
ax[0].set_ylabel("Count")

# QBER chart
ax[1].bar(["Correct Bits", "Errors (QBER)"], [len(alice_key) * (1 - qber), len(alice_key) * qber], color=["blue", "orange"])
ax[1].set_title(f"QBER: {qber:.2%}")
ax[1].set_ylabel("Bits")

plt.suptitle("BB84 with Eavesdropper (Eve) Simulation")
plt.tight_layout()
plt.show()
