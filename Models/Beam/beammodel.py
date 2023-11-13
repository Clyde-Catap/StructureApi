from pydantic import BaseModel
from typing import List
from Models.Beam.force import Forces


class BeamDataResponse(BaseModel):
    beam_type: str
    total_beam_length: int | float
    forces: List[Forces]
