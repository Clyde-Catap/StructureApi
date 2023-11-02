from Operations.Beam.beam import Beam
from Operations.Statics.forces import Force


class BeamSolver:
    def __init__(self, *args: Force, unknown_force_distance):
        self.unknownForceValue = 0
        self.unknownForceDistance = unknown_force_distance
        self.force = args

    def singlePointLoadReactions(self):
        return

    def uniformLoadReactions(self):
        return

    def variableLoadReactions(self):
        return