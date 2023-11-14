from fastapi import FastAPI
from Models.Beam.beammodel import BeamDataResponse
from Operations.Statics.Forces.singlepointforce import SinglePointForce
from Operations.Solver.Beam.simplysupportedbeamsolver import SimplySupportedBeamSolver
from Operations.Solver.Beam.simplysupportedbeamsolver import UniformLoadForce
from Operations.Solver.Beam.simplysupportedbeamsolver import TrapezoidalLoadForce
from Operations.Solver.Beam.simplysupportedbeamsolver import TriangleLoadForce

import random
import logging



app = FastAPI()

@app.get("/")
async def root():
    return {"www": 'working', 'this is data': 0}

@app.post("/beam/")
async def beam(Beam: BeamDataResponse):
    if Beam.beam_type == "simply_supported":

        simplySupportedBeam = SimplySupportedBeamSolver()
        totalReactionAtOrigin = 0
        totalReactionAtEnd = 0

        for force in Beam.forces:

            if force.force_type == "single":
                singleForce = SinglePointForce(magnitude=
                                               force.force_parts.magnitude,
                                               distance=
                                               force.force_parts.distance)
                singleForceReactions = simplySupportedBeam.singlePointLoadReactions(singleForce,
                                                                                    Beam.total_beam_length)
                totalReactionAtOrigin += singleForceReactions["Reaction_at_origin"]
                totalReactionAtEnd += singleForceReactions["Reaction_at_end"]


            if force.force_type == "uniform":
                uniformForce = UniformLoadForce(uniform_magnitude=force.force_parts.magnitude,
                                                distance_to_centroid=force.force_parts.distance_to_centroid,
                                                length_of_uniform_load=force.force_parts.length_of_uniform_load)

                uniformForceReactions = simplySupportedBeam.uniformLoadReactions(uniformForce,
                                                                                 Beam.total_beam_length)
                totalReactionAtOrigin += uniformForceReactions["Reaction_at_origin"]
                totalReactionAtEnd += uniformForceReactions["Reaction_at_end"]


            if force.force_type == "triangle":
                triangleForce = TriangleLoadForce(load_magnitude=
                                                  force.force_parts.magnitude,
                                                  distance_of_max_to_origin=
                                                  force.force_parts.distance_of_max_to_origin,
                                                  distance_of_min_to_origin=
                                                  force.force_parts.distance_of_min_to_origin,
                                                  length_of_load=force.force_parts.length_of_load,
                                                  is_max_near_origin=force.force_parts.is_max_near_origin)

                triangleForceReactions = simplySupportedBeam.triangleLoadReactions(triangleForce,
                                                                                   Beam.total_beam_length)
                totalReactionAtOrigin += triangleForceReactions["Reaction_at_origin"]
                totalReactionAtEnd += triangleForceReactions["Reaction_at_end"]

            if force.force_type == "trapezoid":
                trapezoidForce = TrapezoidalLoadForce(load_magnitude=force.force_parts.magnitude,
                                                      distance_of_min_lower_load_to_origin=
                                                      force.force_parts.distance_of_min_lower_load_to_origin,
                                                      distance_of_max_lower_load_to_origin=
                                                      force.force_parts.distance_of_max_lower_load_to_origin,
                                                      distance_of_max_upper_load_to_origin=
                                                      force.force_parts.distance_of_max_upper_load_to_origin,
                                                      distance_of_min_upper_load_to_origin=
                                                      force.force_parts.distance_of_min_upper_load_to_origin)

                trapezoidForceReactions = simplySupportedBeam.trapezoidalLoadReactions(trapezoidForce,
                                                                                       Beam.total_beam_length)
                totalReactionAtOrigin += trapezoidForceReactions["Reaction_at_origin"]
                totalReactionAtEnd += trapezoidForceReactions["Reaction_at_end"]

    return {"Reaction_at_origin": totalReactionAtOrigin, "Reaction_at_end": totalReactionAtEnd}

# TEST CASES TOMMORROW
