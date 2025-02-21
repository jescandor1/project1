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


def left_endpoint(x_vals: np.ndarray, func: np.ufunc)->float:

    difference = np.diff(x_vals)
    height = func(x_vals[:-1])
    approx = np.sum(difference * height)
    return approx


def simpson(x_vals: np.ndarray, func: np.ufunc) -> float:

    h = np.diff(x_vals)[0]
    f_vals = func(x_vals)

    integral = f_vals[0] + f_vals[-1]
    integral += 4 * np.sum(f_vals[1:-1:2])
    integral += 2 * np.sum(f_vals[2:-1:2])

    return (h / 3) * integral

import numpy as np
func = np.sin
x_vals = np.linspace(0, np.pi, 10001)
simpson_sum = simpson(x_vals, func)
print(f"Simpson's: {simpson_sum}")

