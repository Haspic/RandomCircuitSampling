
import numpy as np
import qutip as q
from qutip_qip.circuit import QubitCircuit
import qutip_qip.operations as qops
import qutip_qip.qubits as qubits
import qutip_qip as qip
from scipy.linalg import expm
import matplotlib.pyplot as plt
from matplotlib import colormaps

""" ##### """

c = QubitCircuit(2, reverse_states=False)
c.add_gate(qops.H(0))
c.add_gate(qops.CNOT(0, 1))
c.add_gate(qops.H(1))
u = c.compute_unitary()

print(u)


from multiple_qubits_circuit import multiple_qubits_circuit
from gates import _0, _1, _I, _X, _Y, _Z
from gates import _S, _sqrt, _H, _CX, _CY, _CZ
from gates import kron

circuit = multiple_qubits_circuit(2)

init = kron(_I, _I)
meas = kron(_I, _I)

circuit.add_gate(_H, index=0)
circuit.add_gate(_CX, index=(0, 1))
circuit.add_gate(_H, index=1)

circuit.set_initial_state(init)
circuit._set_measurement_state(meas)
result = circuit.get_state()

print("")
print(result)
