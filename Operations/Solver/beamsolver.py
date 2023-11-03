from Operations.Beam.beam import Beam
from Operations.Statics.forces import Force
from sympy import symbols, solve, Eq


class BeamSolver:

    @staticmethod
    def singlePointLoadReactions(single_point_load: Force, total_beam_length):
        # Reaction 1 : Reaction at Origin  = R1
        # Reaction 2 : Reaction at End = R2
        # Load : Single point Load = P

        R1, R2 = symbols('R1 R2')
        P = single_point_load.magnitude
        L = total_beam_length
        X1 = single_point_load.distance
        X2 = L - single_point_load.distance

        # # Summation of forces vertical
        SumV = Eq(R1 + R2, P)

        # # Moment at origin
        Mo = Eq(P*X1, R2*L)

        Reactions = solve((SumV,Mo), (R1, R2))

        return Reactions

    @staticmethod
    def uniformLoadReactions(self):
        return

    @staticmethod
    def variableLoadReactions(self):
        return