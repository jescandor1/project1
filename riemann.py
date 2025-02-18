import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc)->float:
    """
    :param x_vals: a one-dimensional NumPy array containing the x-values used in approximating the integral
    :param func: function to approximate the integral
    :return: sum approximation using the left endpoint
    """
    difference = np.diff(x_vals)
    height = func(x_vals[:-1])
    approx = np.sum(difference * height)
    return approx

def trapezoid(x_vals: np.ndarray, func: np.ufunc) -> float:
    """
    Approximates the integral using the Trapezoidal Rule without loops.
    """
    width = (x_vals[1:] - x_vals[:-1])
    return np.sum((func(x_vals[:-1]) + func(x_vals[1:])) / 2 * width)
