import math



class UniformLoadForce:

    def __init__(self, uniform_magnitude: int | float, distance_to_centroid: int | float, length_of_uniform_load: int | float):
        self.uniform_magnitude = float(uniform_magnitude)
        self.distance_to_centroid = float(distance_to_centroid)
        self.length_of_uniform_load = float(length_of_uniform_load)

    def singleLoadConversion(self):
        return self.uniform_magnitude * self.length_of_uniform_load

    def distanceToCentroid(self):
        return self.distance_to_centroid

