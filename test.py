from Operations.Solver.beamsolver import BeamSolver
from Operations.Statics.Forces.singlepointforce import SinglePointForce
from Operations.Statics.Forces.uniformloadforce import UniformLoadForce

beam = BeamSolver()
SingleLoad = SinglePointForce(magnitude=6, distance=6)
SingleLoadReactions = beam.singlePointLoadReactions(SingleLoad, 10)
print(f"Single Point Load: {SingleLoadReactions}")

UniformLoadForceConstant = UniformLoadForce(uniform_magnitude=6, distance_to_centroid=5, length_of_uniform_load=10)
UniformLoadReactions = beam.uniformLoadReactions(UniformLoadForceConstant, 10)
print(f"Unform Load Whole Length: {UniformLoadReactions}")

UniformLoadForceLeft = UniformLoadForce(uniform_magnitude=6, distance_to_centroid=3, length_of_uniform_load=6)
UniformLoadReactionsLeft = beam.uniformLoadReactions(UniformLoadForceLeft, 10)
print(f"Unform Load Whole Length: {UniformLoadReactionsLeft}")

