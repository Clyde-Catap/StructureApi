from Operations.Solver.beamsolver import BeamSolver
from Operations.Statics.Forces.singlepointforce import SinglePointForce
from Operations.Statics.Forces.uniformloadforce import UniformLoadForce
from Operations.Statics.Forces.triangleloadforce import TriangleLoadForce
from Operations.Statics.Forces.trapezoidalloadforce import TrapezoidalLoadForce

beam = BeamSolver()
SingleLoad = SinglePointForce(magnitude=6, distance=6)
SingleLoadReactions = beam.singlePointLoadReactions(SingleLoad, 10)
print(f"Single Point Load: {SingleLoadReactions}")

UniformLoadForceConstant = UniformLoadForce(uniform_magnitude=6, distance_to_centroid=5, length_of_uniform_load=10)
UniformLoadReactions = beam.uniformLoadReactions(UniformLoadForceConstant, 10)
print(f"Uniform Load Whole Length: {UniformLoadReactions}")

UniformLoadForceLeft = UniformLoadForce(uniform_magnitude=6, distance_to_centroid=3, length_of_uniform_load=6)
UniformLoadReactionsLeft = beam.uniformLoadReactions(UniformLoadForceLeft, 10)
print(f"Uniform Load Whole Length: {UniformLoadReactionsLeft}")

TriangleLoadFull = TriangleLoadForce(load_magnitude=6, length_of_load=10, distance_of_min_to_origin=0, distance_of_max_to_origin=0, is_max_near_origin=True)
TriangleLoadReactions = beam.triangleLoadReactions(TriangleLoadFull, 10)
print(f"Triangle Load Whole Length: {TriangleLoadReactions}")

TriangleLoadPartial = TriangleLoadForce(load_magnitude=6, length_of_load=5, distance_of_min_to_origin=2, distance_of_max_to_origin=7, is_max_near_origin=True)
TriangleLoadReactionsPartial = beam.triangleLoadReactions(TriangleLoadPartial, 10)
print(f"Triangle Load Partial Length: {TriangleLoadReactionsPartial}")

TrapezoidalLoad = TrapezoidalLoadForce(load_magnitude=6, distance_of_min_lower_load_to_origin=0, distance_of_max_lower_load_to_origin=10, distance_of_min_upper_load_to_origin=2, distance_of_max_upper_load_to_origin=8)
TrapezoidalLoadReactions = beam.trapezoidalLoadReactions(TrapezoidalLoad, 10)
print(f"Trapezoidal Load: {TrapezoidalLoadReactions}")