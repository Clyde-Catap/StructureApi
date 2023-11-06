class Beam:

    # forces added for the function must be the absolute value and faces one direction
    @staticmethod
    def totalVerticalPositiveForces(*args):
        totalPositiveForces = 0

        for value in range(len(args)):
            totalPositiveForces += float(args[value])

        return totalPositiveForces

    @staticmethod
    def totalVerticalNegativeForces(*args):
        totalNegativeForces = 0

        for value in range(len(args)):
            totalNegativeForces += float(args[value])

        return totalNegativeForces

    @staticmethod
    def totalHorizontalPositiveForces(*args):
        totalPostitiveForces = 0

        for value in range(len(args)):
            totalPostitiveForces += float(args[value])

        return totalPostitiveForces

    @staticmethod
    def totalHorizontalNegativeForces(*args):
        totalNegativeForces = 0

        for value in range(len(args)):
            totalNegativeForces += float(args[value])

        return totalNegativeForces

    @staticmethod
    def Moment(force, distance):
        return force * distance