"""
Oracle for simple Grover's Algorith implementation
"""

import numpy as np
from numpy.linalg import norm
import cmath
import matplotlib.pyplot as plt
import sys
sys.path.append("..")
try:
    from src.sparse_matrix import SparseMatrix
    from src.quantum_register import QuantumRegister
    from src.quantum_operator.py import Operator
except:
    from sparse_matrix import SparseMatrix
    from quantum_register import QuantumRegister
    from quantum_operator import Operator

class Oracle(Operator):
    """
    The oracle searches the quantum register and multiples states that fulfil the problem condition by -1
    """
    def __init__(self, n_qubits: int=1):
        dimension = 2**n_qubits
        base = np.zeros((dimension,dimension))
        for i in range(dimension):
            if (i % 5 == 0):
                base[i][i] = -1
            else:
                base[i][i] = 1

        super(Oracle, self).__init__(n_qubits, base)

    def showit(self):

        print(self)




    

    