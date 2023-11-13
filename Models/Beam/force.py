from pydantic import BaseModel
from Models.Beam.forceparts import ForceParts

class Forces(BaseModel):

    force_type: str
    force_parts: ForceParts
