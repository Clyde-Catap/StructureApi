import math


class SinglePointForce:
    def __init__(self, magnitude: int | float, distance: int | float):
        self.magnitude = float(magnitude)
        self.distance = float(distance)

    def forceMagnitude(self):
        # magnitude =  scalar value of force
        return self.magnitude

    def forceDistance(self):
        # distance = distance from (0,0) origin in cartesian plane from the centroid of the object
        return self.distance
