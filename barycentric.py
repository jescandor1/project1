










import numpy as np
def get_cartesian_coordinates (triangle_coordinates: np.array, barycentric_coordinates: np.array)-> np.array:
    """Triangle_coordinates are a 2x3 array (coeff matrix), Barycentric_coordinates are a 1d array (lamda1, lamda2,
    lamda3)
    """
    point_coordinates = np.dot(barycentric_coordinates, triangle_coordinates)
    """Point coordinates is the dot product of a 2x3 matrix and a 1x3 matrix to make a 1x2 matrix (x,y), also referred
    to as point coordinates"""
    return point_coordinates # (x,y)
