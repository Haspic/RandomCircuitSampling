from qcs import kron, gates, circuit

from qcs.gates import _0, _1, _I, _X, _Y, _Z
from qcs.gates import _S, _sqrt, _H, _CX, _CY, _CZ

c = circuit(2)

init = kron(_0, _0)
meas = kron(_1, _1)

c.add_gate(_H, index=0)
c.add_gate(_CX, index=(0, 1))
c.add_gate(_H, index=1)

c.set_initial_state(init)

# Get matrix form before dot product with meas and init state
# c._set_measurement_state(meas)
# result = c.get_state()

# Get prob of given meas state
c.get_probabilities(meas)
