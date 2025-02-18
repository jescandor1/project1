import numpy as np

def trapezoid(x_vals: np.ndarray, func: np.ufunc) -> float:
    """
    Approximates the integral using the Trapezoidal Rule without loops.
    """
    width = (x_vals[:-1] - x_vals[1:])
    return np.sum((func(x_vals[:-1]) + func(x_vals[1:])) / 2 * width)
