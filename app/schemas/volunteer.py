from datetime import datetime
from pydantic import BaseModel, EmailStr
from app.schemas.enums import (
    DesiredRoleEnum,
    AvailabilityEnum,
    StatusEnum,
)


class VolunteerBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    desired_role: DesiredRoleEnum
    availability: AvailabilityEnum
    status: StatusEnum


class VolunteerResponse(VolunteerBase):
    id: int
    registration_date: datetime

    class Config:
        from_attributes = True
