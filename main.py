
import numpy as np
import matplotlib.pyplot as plt
from gates import _0, _1, _I, _X, _Y, _Z
from gates import _S, _sqrt, _H, _CX, _CY, _CZ

from gates import kron

""" SINGLE LINE CIRCUIT """

from single_line_circuit import single_line_circuit

# Initial state
# init = np.array([0, 1])

# Measurement state
# meas = np.array([1, 0])

# circuit = single_line_circuit()
# circuit.set_initial_state(init)
# circuit.set_gates(X, X, X)
#
# print(circuit.make_measurement(meas))

""" MULTIPLE LINE CIRCUIT """

from multiple_qubits_circuit import multiple_qubits_circuit


circuit = multiple_qubits_circuit(4)

init = kron(_0, _0, _0, _0)
meas = kron(_0, _0, _0, _0)

circuit.add_gate(_Z, index=0)
circuit.add_gate(_X, index=1)
circuit.add_gate(_H, index=3)

circuit.add_gate(_CX, index=(1, 2))

circuit.add_gate(_H, index=1)
circuit.add_gate(_Y, index=2)

circuit.add_gate(_CZ, index=(1, 3))
circuit.add_gate(_CX, index=(2, 0))

# circuit.add_gate(_H, index=3)

circuit.set_initial_state(init)

# measurements = [
#     kron(_0, _0, _0, _0),
#     kron(_0, _1, _0, _0),
#     kron(_0, _0, _0, _1),
#     kron(_0, _1, _0, _1),
#     kron(_1, _1, _1, _1)
# ]
#
# for measurement in measurements:
#
#     r = circuit.get_probabilities(measurement)
#     print("Measurement:", measurement, "- Probabilities:", round(r, 5))

states = []
for _ in range(100):
    m = circuit.make_measurement()
    states.append("".join([elt.name for elt in m]))
plt.hist(states)
plt.show()
