import math



class beam:
    # forces added for the function must be the absolute value and faces one direction
    @staticmethod
    def positiveForces(*args):
        totalPositiveForces = 0

        for value in range(len(args)):
            totalPositiveForces += float(args[value])

        return totalPositiveForces

    @staticmethod
    def negativeForces(*args):
        totalNegativeForces = 0

        for value in range(len(args)):
            totalNegativeForces += float(args[value])

        return totalNegativeForces