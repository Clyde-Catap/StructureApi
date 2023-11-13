from pydantic import BaseModel
from typing import List, Optional


class ForceParts(BaseModel):

    # Single Load
    magnitude: float
    distance: Optional[float]

    # Uniform Load
    distance_to_centroid: Optional[float]
    length_of_uniform_load: Optional[float]

    # Triangular Load
    length_of_load: Optional[float]
    distance_of_min_to_origin: Optional[float]
    distance_of_max_to_origin: Optional[float]
    is_max_near_origin: Optional[bool]

    # Trapezoidal Load
    distance_of_min_lower_load_to_origin: Optional[float]
    distance_of_max_lower_load_to_origin: Optional[float]
    distance_of_min_upper_load_to_origin: Optional[float]
    distance_of_max_upper_load_to_origin: Optional[float]
