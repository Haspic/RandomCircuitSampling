
import numpy as np

""" ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### """

def kron(*mat):
    """Kronecker product of N number of matrices"""

    product = mat[0]

    for i in range(1, len(mat)):
        product = np.kron(product, mat[i])

    return product


""" ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### """


class Gate(object):

    def __init__(self, mat: np.ndarray, activators=None):
        self.mat = mat
        self.activators = activators

    def get_mat(self):
        return self.mat.copy()

# class SimpleGate(Gate):
#
#     def __init__(self, mat: np.ndarray):
#         super().__init__(mat)
#
#
# class ControlledGate(Gate):
#
#     def __init__(self, mat: np.ndarray):
#         super().__init__(mat)


""" ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### """


_0 = Gate(np.array([1, 0]))
_1 = Gate(np.array([0, 1]))

_I = Gate(np.array([[1, 0],
                    [0, 1]]))

_X = Gate(np.array([[0, 1],
                    [1, 0]]))
# _Y = Gate(np.array([[0, -1j],
#                     [1j, 0]]))
# _Z = Gate(np.array([[1, 0],
#                     [0, -1]]))

_CX = Gate(np.array([[0, 1],  # X gate
                     [1, 0]]),
           np.array([[[1, 0],  # |0> <0| activator
                      [0, 0]],
                     [[0, 0],  # |1> <1| activator
                      [0, 1]]]))

# _CY = Gate(np.array([[1, 0, 0, 0],
#                      [0, 1, 0, 0],
#                      [0, 0, 0, -1j],
#                      [0, 0, 1j, 0]]))
# _CZ = Gate(np.array([[1, 0, 0, 0],
#                      [0, 1, 0, 0],
#                      [0, 0, 1, 0],
#                      [0, 0, 0, -1]]))

