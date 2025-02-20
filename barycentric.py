import numpy as np

def get_barycentric_coordinates(triangle_coordinates: [], point_coordinates: [] ) -> []:
    triangle_coordinates += [1, 1, 1]
    point_coordinates += [1]
    barycentric_coordinates = np.linalg.solve(triangle_coordinates, point_coordinates)
    return barycentric_coordinates