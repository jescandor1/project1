import numpy as np

def get_barycentric_coordinates(triangle_coordinates: np.array, point_coordinates: np.array ) -> np.array:
    """
    :param triangle_coordinates: 2x3 array (coeff matrix)
    :param point_coordinates: 1d array (x, y)
    :return: 1d array (lambda1, lambda2, lambda3)
    """
    triangle_coordinates += [1, 1, 1]
    point_coordinates += [1]
    barycentric_coordinates = np.linalg.solve(triangle_coordinates, point_coordinates)
    return barycentric_coordinates

def get_cartesian_coordinates (triangle_coordinates: np.array, barycentric_coordinates: np.array)-> np.array:
    """Triangle_coordinates are a 2x3 array (coeff matrix), Barycentric_coordinates are a 1d array (lamda1, lamda2,
    lamda3)
    """
    cartesian_coordinates = np.dot(barycentric_coordinates, triangle_coordinates)
    """Cartesian coordinates is the dot product of a 2x3 matrix and a 1x3 matrix to make a 1x2 matrix (x,y), also referred
    to as cartesian/point coordinates"""
    return cartesian_coordinates # (x,y)
    
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
