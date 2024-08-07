
import numpy as np
from gates import _0, _1, _I, _X


class multiple_qubits_circuit(object):

    def __init__(self, circuit_size):
        self.size = circuit_size

        self.gates = np.array([])
        self.initial_state = np.zeros(circuit_size * 2)
        self.measurement_state = None

    """ ##### ##### ##### ##### ##### ##### """
    def add_initial_state(self, initial_state):
        self.initial_state = initial_state

    def add_measurement_state(self, measurement_state):
        self.measurement_state = measurement_state

    def add_gate(self, gate, index: int or list or tuple) -> None:
        """
        Add a gate to the circuit.

        :param gate: gate object to be added
        :param index: index of the circuit line (from top to bottom)
        :return: None
        """

        if type(index) is int:
            # Simple gate case
            # Tensor product between all circuit lines with either identity matrix or with gate matrix

            # The gate matrix
            result = gate.get_mat()

            for i in range(self.size):
                # If qubit is before gate (from top to bottom)
                if i < index:
                    tensorProduct = np.kron(_I, result)
                # If qubit is after gate (from top to bottom)
                elif i > index:
                    tensorProduct = np.kron(result, _I)

        elif type(index) in [list, tuple]:
            # Complex/controlled gate case

            result = np.zeros((2 ** self.size) ** 2).reshape(2 ** self.size, 2 ** self.size)

            # FIRST activator matrix
            tensorProduct = gate.activators[0]

            for i in range(self.size):
                # If qubit is before gate (from top to bottom)
                if i < index[0]:
                    tensorProduct = np.kron(_I, tensorProduct)
                # If qubit is after gate (from top to bottom)
                elif i > index[0]:
                    tensorProduct = np.kron(tensorProduct, _I)

            result += tensorProduct

            # SECOND activator matrix
            tensorProduct = gate.activators[0]

            for i in range(self.size):
                # If qubit is before gate (from top to bottom)
                if i < index[0]:
                    tensorProduct = np.kron(_I, tensorProduct)
                # If qubit is after gate (from top to bottom)
                elif i > index[0]:
                    tensorProduct = np.kron(tensorProduct, _I)
                elif i == index[1]:
                    tensorProduct = np.kron(tensorProduct, gate.get_mat())
                elif i > index[1]:
                    tensorProduct = np.kron(tensorProduct, _I)

            result += tensorProduct

        else:
            raise TypeError("Index must be an int, list or tuple")

        # Add final tensor product to dot product step
        self.gates = np.append(self.gates, result)

    def get_probabilities(self):

        if self.measurement_state is None:
            raise ValueError("Measurement state is not defined")

        result = self.measurement_state

        for gate in self.gates[::-1]:
            result = np.dot(result, gate)

        result = np.dot(result, self.initial_state)

        return np.abs(result) ** 2

            #
            # if str(gate) == "CX": # (Make it general case later)
            #
            #     tensorProduct = _I.get_mat()
            #
            #     for i in range(self.size):
            #
            #         # if i outside of index, do outer product with identity matrix
            #         if i <= index[0] or i > index[1]:
            #             tensorProduct = np.kron(tensorProduct, _I.get_mat())
            #
            #         else:
            #
            #
            #
            #             # if i == end index, do outer product with appropriate matrix
            #             elif i == index[1]:
            #                 tensorProduct = np.kron(tensorProduct, _X.get_mat())
            #
            #             # if i inside of index, do
            #             elif
            #
            #     # Add final tensor product to dot product step
            #     self.gates = np.append(self.gates, tensorProduct)

    # def set_gates(self, *gates: np.ndarray):
    #     """
    #     Sets up the list of gates in order from initial state to measured state
    #     :param gates: list of gates
    #     """
    #     self.gates = gates
    #
    # def set_initial_state(self, initial_state):
    #     self.initial_state = initial_state
    #
    # """ ##### ##### ##### ##### ##### ##### """
    #
    # def _compute_line(self, measured_state):
    #
    #     matrix_operation = measured_state
    #
    #     for gate in self.gates:
    #         matrix_operation = np.dot(gate, matrix_operation)
    #
    #     state_coefficient = np.dot(matrix_operation, self.initial_state)
    #     probability = np.abs(state_coefficient)**2
    #
    #     return probability
    #
    # def make_measurement(self, measured_state):
    #     return self._compute_line(measured_state)
