### Quantum Circuit Simulator (qcs)

All code is included in the "packageForm" file. Download this file and install the package onto your python environment using "pip install ." once in the "packageForm" directory.

Usage example:

```
from qcs import circuit, kron
from qcs.gates import _0, _1, _I, _X, _Y, _Z
from qcs.gates import _S, _sqrt, _H, _CX, _CY, _CZ

circuit = multiple_qubits_circuit(2) # number of qubits

# kron function takes an arbitrary amount of arguments
init = kron(_0, _0)
meas = kron(_0, _0)

circuit.add_gate(_H, index=0)
circuit.add_gate(_CX, index=(0, 1))
circuit.add_gate(_H, index=1)

circuit.set_initial_state(init)

# circuit._set_measurement_state(meas)
# result = circuit.get_state()

r = circuit.get_probabilities(measurement)
```

