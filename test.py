from sympy import symbols, solve, Eq
from Operations.Solver.beamsolver import BeamSolver
from Operations.Statics.forces import Force

f1 = Force(magnitude=6, distance=6)
beam = BeamSolver()

Rxn = beam.singlePointLoadReactions(f1, 10)
print(Rxn)
