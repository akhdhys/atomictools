# pylint: disable=E0102

import numpy as np
from numpy.linalg import norm
from multimethod import multimethod

from atomictools.lattice import move_to_wigner_seitz


@multimethod
def distance_matrix(pos1: np.ndarray, pos2: np.ndarray):
    return np.array([[norm(p - q) for p in pos2] for q in pos1])


@multimethod
def distance_matrix(pos1: np.ndarray, pos2: np.ndarray, ws: np.ndarray):
    def tows(r):
        move_to_wigner_seitz(r, ws)
        return r
    return np.array([[norm(tows(p - q)) for q in pos2] for p in pos1])
