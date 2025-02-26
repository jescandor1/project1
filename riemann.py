import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc)->float:
    """
    Riemann approximation using the left endpoint
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
    """
    Calculates the base of each individual trapezoid by taking the last term of the array and subtracting the prior
    term, allowing me to get a base value for each trapezoid
    
    Takes the height of each point and adds the heights together. Then divides the heights by 2 to get the average
    height. Average height is then multiplied by the width or base to get the area of the trapezoid. Areas are then
    summed together.
    """
    return np.sum((func(x_vals[:-1]) + func(x_vals[1:])) / 2 * width)


def simpson(x_vals: np.ndarray, func: np.ufunc) -> float:
    """ Approximates the integral using Simpson's rule. Uses a one-dimensional array to find the area to integrate
    over. Then takes a specified function to approximate the integral using Simpson's rule

    A float value will be returned that approximates the integral/area under the curve that is being evaluated.
    """
    a = x_vals[0]
    b = x_vals[-1]
    midpoint = (a + b) / 2
    h = (b - a) / 6
    integral = h * (func(a) + 4*func(midpoint) + func(b))
    return integral



