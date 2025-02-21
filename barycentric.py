import numpy as np

def get_barycentric_coordinates(triangle_coordinates: np.array, point_coordinates: np.array ) -> np.array:
    """
    :param triangle_coordinates: 2x3 array (coeff matrix)
    :param point_coordinates: 1d array (x, y)
    :return: 1d array (lambda1, lambda2, lambda3)
    """
    triangle_coordinates = np.hstack((triangle_coordinates, np.ones((3, 1))))
    point_coordinates = np.append(point_coordinates, 1)
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
    
def is_inside_triangle (triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> bool:
    barycentric_coordinates = get_barycentric_coordinates(triangle_coordinates, point_coordinates)

    return np.all(barycentric_coordinates >= 0) and np.all(barycentric_coordinates <= 1)

