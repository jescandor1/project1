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