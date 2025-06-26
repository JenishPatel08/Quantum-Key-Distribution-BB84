# 🔐 Quantum Key Distribution using BB84 Protocol (with Eve Simulation)

This project demonstrates the **BB84 Quantum Key Distribution Protocol** using Python and Qiskit, including a simulation of a real-world **eavesdropper (Eve)**. It shows how quantum physics prevents secure keys from being intercepted, and how errors introduced by Eve are detected using **QBER (Quantum Bit Error Rate)**.

---

## 📌 Features

- ✅ Simulates the BB84 protocol between Alice and Bob
- 🕵️ Adds a malicious Eve who tries to intercept and measure qubits
- 📉 Calculates and visualizes QBER (Quantum Bit Error Rate)
- 📊 Visualizes:
  - Basis matching between Alice & Bob
  - Bit errors caused by Eve

---

## 🧠 How BB84 Works (In Simple Terms)

1. **Alice** generates random bits and bases (Z or X)
2. She sends qubits based on this info to **Bob**
3. **Eve** tries to intercept, but disturbs the qubits if her guess is wrong
4. **Bob** measures using his own random bases
5. Alice and Bob keep bits where their bases matched
6. If Eve interfered, **QBER** will be high — proving a spy was watching

---

## 📊 Example Output (Visualization)

| Chart | Description |
|-------|-------------|
| Basis Matching | Shows how often Alice and Bob used the same basis |
| QBER Chart     | Shows how many bits were correct vs. tampered |

![QBER Visualization](https://github.com/JenishPatel08/Quantum-Key-Distribution-BB84/blob/a8fc483960134a46c99bdeccf32b84fbe7104533/QuantumBB84/image/qber_plot.png)

---

## 📚 Learn More

- [IBM Qiskit Documentation](https://qiskit.org/documentation/)
- [BB84 Protocol – Wikipedia](https://en.wikipedia.org/wiki/BB84)
- [My Blog: BB84 Quantum Key Distribution Explained](https://jenishpatel.hashnode.dev/bb84-quantum-key-distribution)

---

🧑‍💻 Author
Made with ❤️ by Jenish Patel
