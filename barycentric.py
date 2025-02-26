import numpy as np

def get_barycentric_coordinates(triangle_coordinates: np.array, point_coordinates: np.array ) -> np.array:
    """
    :param triangle_coordinates: 2x3 array (coeff matrix)
    :param point_coordinates: 1d array (x, y)
    :return: 1d array (lambda1, lambda2, lambda3)
    """
    x1, x2, x3 = triangle_coordinates[0]
    y1, y2, y3 = triangle_coordinates[1]
    A = np.array([[x1, x2, x3],
                  [y1, y2, y3],
                  [1, 1, 1]])
    b = np.array([point_coordinates[0], point_coordinates[1], 1])
    barycentric_coordinates = np.linalg.solve(A, b)
    #print(barycentric_coordinates)
    return barycentric_coordinates

def get_cartesian_coordinates (triangle_coordinates: np.array, barycentric_coordinates: np.array)-> np.array:
    """
    Triangle_coordinates are a 2x3 array (coeff matrix),
    Barycentric_coordinates are a 1d array (lamda1, lamda2, lamda3)
    """
    x1, x2, x3 = triangle_coordinates[0]
    y1, y2, y3 = triangle_coordinates[1]
    """Cartesian coordinates is the dot product of a 2x3 matrix and a 1x3 matrix to make a 1x2 matrix (x,y), also referred
        to as cartesian/point coordinates"""
    x = barycentric_coordinates[0] * x1 + barycentric_coordinates[1] * x2 + barycentric_coordinates[2] * x3
    y = barycentric_coordinates[0] * y1 + barycentric_coordinates[1] * y2 + barycentric_coordinates[2] * y3
    return np.array([x, y])

def is_inside_triangle (triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> bool:
    """Determines whether a given point is inside a triangle using barycentric coordinates.
by taking a 2x3 matrix of the triangles vertexes to see if coordinates lie within vertexes  """
    triangle_coordinates = np.reshape(triangle_coordinates, (2, 3))
    barycentric_coordinates = get_barycentric_coordinates(triangle_coordinates, point_coordinates)

    return np.all(barycentric_coordinates >= 0) and np.all(barycentric_coordinates <= 1)
"""Will return a bool statement of either True or False which will be shown as a point on a graph. Points that lie
within the triangle are green and True while points that lie outside the triangle are red and False"""