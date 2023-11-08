import math




class TriangleLoadForce:

    def __init__(self, load_magnitude, length_of_load, distance_of_min_to_origin, distance_of_max_to_origin, is_max_near_origin: bool):
        self.load_magnitude = float(load_magnitude)
        self.length_of_load = float(length_of_load)
        self.distance_of_min_to_origin = float(distance_of_min_to_origin)
        self.distance_of_max_to_origin = float(distance_of_max_to_origin)
        self.is_max_near_origin = is_max_near_origin

    def singleLoadConversion(self):
        # 1/3 base * height
        return (1/2) * self.length_of_load * self.load_magnitude

    def distanceToCentroid(self):
        if self.is_max_near_origin:
            return self.distance_of_max_to_origin + ((1/3) * self.length_of_load)
        else:
            return self.distance_of_min_to_origin + ((2/3) * self.length_of_load)






