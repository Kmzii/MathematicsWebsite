import numpy as np


def heaviside_function(x):
    return 0.5 * (np.sign(x) + 1)