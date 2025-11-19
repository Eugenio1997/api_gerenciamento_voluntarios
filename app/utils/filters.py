from typing import Optional
from pydantic import BaseModel
from app.schemas.enums import (
    DesiredRoleEnum,
    AvailabilityEnum,
    StatusEnum,
)


class VolunteerFilters(BaseModel):
    desired_role: Optional[DesiredRoleEnum] = None
    availability: Optional[AvailabilityEnum] = None
    status: Optional[StatusEnum] = None
