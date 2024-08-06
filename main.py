
import numpy as np
from single_line_circuit import single_line_circuit

# Initial state
I = np.array([0, 1])

# Gates
X = np.array([[0, 1], [1, 0]])

# Measurement state
M = np.array([0, 1])

circuit = single_line_circuit()
circuit.set_initial_state(I)
circuit.set_gates(X)

print(circuit.make_measurement(M))
