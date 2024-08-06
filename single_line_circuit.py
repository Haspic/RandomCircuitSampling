
import numpy as np


class single_line_circuit(object):

    def __init__(self):
        self.gates = []
        self.initial_state = np.array([0, 0])

    """ ##### ##### ##### ##### ##### ##### """

    def set_gates(self, *gates: np.ndarray):
        """
        Sets up the list of gates in order from initial state to measured state
        :param gates: list of gates
        """
        self.gates = gates

    def set_initial_state(self, initial_state):
        self.initial_state = initial_state

    """ ##### ##### ##### ##### ##### ##### """

    def _compute_line(self, measured_state):

        matrix_operation = measured_state

        for gate in self.gates:
            matrix_operation = np.dot(gate, matrix_operation)

        state_coefficient = np.dot(matrix_operation, self.initial_state)
        probability = np.abs(state_coefficient)**2

        return probability

    def make_measurement(self, measured_state):
        return self._compute_line(measured_state)
