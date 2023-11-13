import math
from Operations.Statics.Forces.uniformloadforce import UniformLoadForce
from Operations.Statics.Forces.triangleloadforce import TriangleLoadForce
from sympy import symbols, solve, Eq


class TrapezoidalLoadForce:

    def __init__(self, load_magnitude: int | float,
                 distance_of_min_lower_load_to_origin: int | float,
                 distance_of_max_lower_load_to_origin: int | float,
                 distance_of_min_upper_load_to_origin: int | float,
                 distance_of_max_upper_load_to_origin: int | float):


        self.load_magnitude = float(load_magnitude)
        self.distance_of_min_lower_load_to_origin = float(distance_of_min_lower_load_to_origin)
        self.distance_of_max_lower_load_to_origin = float(distance_of_max_lower_load_to_origin)
        self.distance_of_min_upper_load_to_origin = float(distance_of_min_upper_load_to_origin)
        self.distance_of_max_upper_load_to_origin = float(distance_of_max_upper_load_to_origin)

        # for the uniform load
        self.uniformLoad = UniformLoadForce(self.load_magnitude,
                                       (self.distance_of_max_upper_load_to_origin - self.distance_of_min_upper_load_to_origin) / 2,
                                       (self.distance_of_max_upper_load_to_origin - self.distance_of_min_upper_load_to_origin))

        # for the left triangle load
        self.leftTriangleLoad = TriangleLoadForce(self.load_magnitude,
                                             (self.distance_of_min_upper_load_to_origin - self.distance_of_min_lower_load_to_origin),
                                             self.distance_of_min_lower_load_to_origin,
                                             self.distance_of_min_upper_load_to_origin,
                                             is_max_near_origin=False)
        # for the right triangle load
        self.rightTriangleLoad = TriangleLoadForce(self.load_magnitude,
                                              (self.distance_of_max_lower_load_to_origin - self.distance_of_max_upper_load_to_origin),
                                              self.distance_of_max_lower_load_to_origin,
                                              self.distance_of_max_upper_load_to_origin,
                                              is_max_near_origin=True)


    def singleLoadConversion(self):
        return (
                self.uniformLoad.singleLoadConversion() +
                self.leftTriangleLoad.singleLoadConversion() +
                self.rightTriangleLoad.singleLoadConversion()
                )

    def distanceToCentroid(self):
        return (self.uniformLoad.length_of_uniform_load/2) + self.leftTriangleLoad.length_of_load
