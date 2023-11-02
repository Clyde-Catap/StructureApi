import math



class beam:

    def __init__(self):
        self.toTalPositiveForces = 0
        self.totalNegativeForces = 0


    # forces added for the function must be the absolute value and faces one direction
    def toTalPositiveForces(*args):
        totalPositiveForces = 0

        for value in range(len(args)):
            totalPositiveForces += float(args[value])

        return totalPositiveForces


    def toTalNegativeForces(*args):
        totalNegativeForces = 0

        for value in range(len(args)):
            totalNegativeForces += float(args[value])

        return totalNegativeForces