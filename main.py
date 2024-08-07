
import numpy as np
from gates import _0, _1, _X, _CX
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


circuit = multiple_qubits_circuit(3)

# init = kron(_0, _0)
# meas = kron(_1, _1)
#
# circuit.add_gate(_X, index=0)
# circuit.add_gate(_CX, index=(0, 1))

# init = kron(_1, _0, _0, _1)
# meas = kron(_0, _1, _1, _0)
#
# circuit.add_gate(_CX, index=(0, 2))
# circuit.add_gate(_X, index=0)
# circuit.add_gate(_X, index=3)
# circuit.add_gate(_CX, index=(1, 2))
# circuit.add_gate(_X, index=1)

init = kron(_1, _1, _1)
meas = kron(_0, _1, _1)

circuit.add_gate(_X, index=0)
circuit.add_gate(_X, index=2)
circuit.add_gate(_CX, index=(1, 2))

circuit.add_initial_state(init)
circuit.add_measurement_state(meas)

r = circuit.get_probabilities()
print(r)
