from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.volunteer import VolunteerBase, VolunteerResponse
from app.utils.filters import VolunteerFilters
from app.services.volunteer_service import (
    create_volunteer,
    get_all_volunteers
)

router = APIRouter(
    prefix="/volunteers",
    tags=["Volunteers"]
)


@router.get("/", response_model=List[VolunteerResponse])
def list_volunteers(filters: VolunteerFilters = Depends()):
    return get_all_volunteers(filters)

@router.post("/", response_model=VolunteerResponse, status_code=201)
def add_volunteer(data: VolunteerBase):
    try:
        return create_volunteer(data)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))