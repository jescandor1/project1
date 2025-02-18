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
    width = (x_vals[1:] - x_vals[:-1])
    """Calculates the base of each individual trapezoid by taking the last term of the array and subtracting the prior
    term, allowing me to get a base value for each trapezoid"""
    return np.sum((func(x_vals[:-1]) + func(x_vals[1:])) / 2 * width)
    """Takes the height of each point and adds the heights together. Then divides the heights by 2 to get the average
     height. Average height is then multiplied by the width or base to get the area of the trapezoid. Areas are then
     summed together"""
