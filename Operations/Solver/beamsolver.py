from Operations.Statics.Forces.singlepointforce import SinglePointForce
from Operations.Statics.Forces.uniformloadforce import UniformLoadForce
from sympy import symbols, solve, Eq


class BeamSolver:

    @staticmethod
    def singlePointLoadReactions(single_point_load: SinglePointForce, total_beam_length):
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
    def uniformLoadReactions(uniform_load: UniformLoadForce, total_beam_length):
        # Reaction 1 : Reaction at Origin  = R1
        # Reaction 2 : Reaction at End = R2
        # Load : Uniform Load = U

        UR1, UR2 = symbols('R1 R2')
        # Uniform Load transformed to Single load
        U = uniform_load.uniform_magnitude*uniform_load.length_of_uniform_load
        L = total_beam_length
        X1 = uniform_load.distance_to_centroid
        X2 = L - uniform_load.distance_to_centroid
        # # Summation of forces vertical
        SumV = Eq(UR1 + UR2, U)

        # # Moment at origin
        Mo = Eq(U*X1, UR2*L)

        Reactions = solve((SumV, Mo), (UR1, UR2))


        return Reactions

    @staticmethod
    def variableLoadReactions(self):
        return