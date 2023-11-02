import math


class Force:
    def __init__(self, magnitude, distance):
        self.magnitude = float(magnitude)
        self.distance = float(distance)

    def forceMagnitude(self):
        # magnitude =  scalar value of force
        return self.magnitude

    def forceDistance(self):
        # distance = distance from (0,0) origin in cartesian plane
        return self.distance
