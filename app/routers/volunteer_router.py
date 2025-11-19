from fastapi import APIRouter, Depends
from typing import List
from app.schemas.volunteer import VolunteerResponse
from app.utils.filters import VolunteerFilters
from app.services.volunteer_service import (
    get_all_volunteers
)

router = APIRouter(
    prefix="/volunteers",
    tags=["Volunteers"]
)


@router.get("/", response_model=List[VolunteerResponse])
def list_volunteers(filters: VolunteerFilters = Depends()):
    return get_all_volunteers(filters)