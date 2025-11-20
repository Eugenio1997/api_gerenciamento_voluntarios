from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.volunteer import VolunteerBase, VolunteerResponse
from app.utils.filters import VolunteerFilters
from app.services.volunteer_service import (
    create_volunteer,
    delete_volunteer,
    get_all_volunteers,
    get_volunteer_by_id,
    update_volunteer
)

router = APIRouter(
    prefix="/volunteers",
    tags=["Volunteers"]
)


@router.get("/", response_model=List[VolunteerResponse])
def list_volunteers_endpoint(filters: VolunteerFilters = Depends()):
    return get_all_volunteers(filters)

@router.get("/{volunteer_id}", response_model=VolunteerResponse)
def list_volunteers_endpoint(volunteer_id: int):
    return get_volunteer_by_id(volunteer_id)

@router.post("/", response_model=VolunteerResponse, status_code=201)
def add_volunteer_endpoint(data: VolunteerBase):
    try:
        return create_volunteer(data)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    
@router.put("/{volunteer_id}")
def update_volunteer_endpoint(volunteer_id: int, data: VolunteerBase):
    return update_volunteer(volunteer_id, data)


@router.delete("/{volunteer_id}", status_code=204)
def delete_volunteer_endpoint(volunteer_id: int):
    return delete_volunteer(volunteer_id)