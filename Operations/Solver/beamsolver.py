from Operations.Statics.Forces.singlepointforce import SinglePointForce
from Operations.Statics.Forces.uniformloadforce import UniformLoadForce
from Operations.Statics.Forces.triangleloadforce import TriangleLoadForce
from Operations.Statics.Forces.trapezoidalloadforce import TrapezoidalLoadForce
from sympy import symbols, solve, Eq


class BeamSolver:

    @staticmethod
    def singlePointLoadReactions(single_point_load: SinglePointForce, total_beam_length):
        # Reaction 1 : Reaction at Origin
        # Reaction 2 : Reaction at End
        # Load : Single point Load = P
        # X1 : Distance of origin to centroid of load
        # X2 : Remaining distance form centroid of load to end

        R1, R2 = symbols('Reaction_at_origin Reaction_at_end')
        P = single_point_load.magnitude
        L = total_beam_length
        X1 = single_point_load.distance
        X2 = L - single_point_load.distance

        # # Summation of forces vertical
        SumV = Eq(R1 + R2, P)

        # # Moment at origin
        Mo = Eq(P*X1, R2*L)

        Reactions = solve((SumV, Mo), (R1, R2))

        return Reactions

    @staticmethod
    def uniformLoadReactions(uniform_load: UniformLoadForce, total_beam_length):
        # Reaction 1 : Reaction at Origin
        # Reaction 2 : Reaction at End
        # Load : Uniform Load = U
        # X1 : Distance of origin to centroid of load
        # X2 : Remaining distance form centroid of load to end

        UR1, UR2 = symbols('Reaction_at_origin Reaction_at_end')
        # Uniform Load transformed to Single load
        U = uniform_load.uniform_magnitude*uniform_load.length_of_uniform_load
        L = total_beam_length
        X1 = uniform_load.distance_to_centroid
        X2 = L - uniform_load.distance_to_centroid

        # Summation of forces vertical
        SumV = Eq(UR1 + UR2, U)

        # Moment at origin
        Mo = Eq(U*X1, UR2*L)

        Reactions = solve((SumV, Mo), (UR1, UR2))


        return Reactions



    #VARIABLE LOADS
    @staticmethod
    def triangleLoadReactions(triangle_load: TriangleLoadForce, total_beam_length):
        # Reaction 1 : Reaction at Origin
        # Reaction 2 : Reaction at End
        # Load : Triangle Load = T
        # X1 : Distance of origin to centroid of load
        # X2 : Remaining distance form centroid of load to end

        TR1, TR2 = symbols('Reaction_at_origin Reaction_at_end')
        # Triangle Load transformed to Single load
        T = (1 / 2) * triangle_load.length_of_load * triangle_load.load_magnitude
        L = total_beam_length

        if triangle_load.is_max_near_origin:

            if triangle_load.length_of_load == L:
                X1 = (1/3) * triangle_load.length_of_load

            else:
                X1 = triangle_load.distance_of_min_to_origin + ((1/3) * triangle_load.length_of_load)

        if not triangle_load.is_max_near_origin:
            if triangle_load.length_of_load == L:
                X1 = (2/3) * triangle_load.length_of_load
            else:
                X1 = triangle_load.distance_of_min_to_origin + ((2/3) * triangle_load.length_of_load)


        X2 = L - X1

        # Summation of forces vertical
        SumV = Eq(TR1 + TR2, T)

        # Moment at origin
        Mo = Eq(T*X1, TR2*L)

        Reactions = solve((SumV, Mo), (TR1, TR2))

        return Reactions
    @staticmethod
    def trapezoidalLoadReactions(trapezoidal_load: TrapezoidalLoadForce, total_beam_length):
        # Reaction 1 : Reaction at Origin
        # Reaction 2 : Reaction at End
        # Load : Trapezoidal Load = T
        # X1 : Distance of origin to centroid of load
        # X2 : Remaining distance form centroid of load to end

        TPR1, TPR2 = symbols('Reaction_at_origin Reaction_at_end')
        # Uniform Load transformed to Single load
        T = trapezoidal_load.singleLoadConversion()
        L = total_beam_length
        X1 = trapezoidal_load.distanceToCentroid()
        X2 = L - trapezoidal_load.distanceToCentroid()

        # Summation of forces vertical
        SumV = Eq(TPR1 + TPR2, T)

        # Moment at origin
        Mo = Eq(T*X1, TPR2*L)

        Reactions = solve((SumV, Mo), (TPR1, TPR2))

        return Reactions
