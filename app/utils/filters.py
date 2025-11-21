from fastapi import Query
from typing import Optional
from app.schemas.enums import DesiredRoleEnum, AvailabilityEnum, StatusEnum


class VolunteerFilters:
    def __init__(
        self,
        desired_role: Optional[DesiredRoleEnum] = Query(
            None,
            alias="cargo_pretendido",
            description="Filtrar pelo cargo pretendido do voluntário."
        ),
        availability: Optional[AvailabilityEnum] = Query(
            None,
            alias="disponibilidade",
            description="Filtrar pela disponibilidade do voluntário."
        ),
        status: Optional[StatusEnum] = Query(
            None,
            alias="status",
            description="Filtrar pelo status do voluntário."
        ),
    ):
        self.desired_role = desired_role
        self.availability = availability
        self.status = status
