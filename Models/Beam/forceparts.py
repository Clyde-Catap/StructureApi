from pydantic import BaseModel, Field
from typing import List, Optional


class ForceParts(BaseModel):

    # Single Load
    magnitude: float = Field(default=0.0)
    distance: Optional[float] = Field(default=0.0)

    # Uniform Load
    distance_to_centroid: Optional[float] = Field(default=0.0)
    length_of_uniform_load: Optional[float] = Field(default=0.0)

    # Triangular Load
    length_of_load: Optional[float] = Field(default=0.0)
    distance_of_min_to_origin: Optional[float] = Field(default=0.0)
    distance_of_max_to_origin: Optional[float] = Field(default=0.0)
    is_max_near_origin: Optional[bool] = Field(default=0.0)

    # Trapezoidal Load
    distance_of_min_lower_load_to_origin: Optional[float] = Field(default=0.0)
    distance_of_max_lower_load_to_origin: Optional[float] = Field(default=0.0)
    distance_of_min_upper_load_to_origin: Optional[float] = Field(default=0.0)
    distance_of_max_upper_load_to_origin: Optional[float] = Field(default=0.0)
