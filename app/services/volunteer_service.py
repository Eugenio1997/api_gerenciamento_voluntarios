from datetime import datetime
from typing import Dict, List

from fastapi import HTTPException
from app.schemas.volunteer import VolunteerBase, VolunteerResponse
from app.utils.filters import VolunteerFilters

DATABASE: List[Dict] = [
    {
        "id": 1,
        "name": "Maria Silva",
        "email": "maria.silva@example.com",
        "desired_role": "analyst",
        "status": "active",
        "availability": "morning",
        "phone": "(11) 91234-5678",
        "active": True,
        "registration_date": datetime.now()
    },
    {
        "id": 2,
        "name": "Carlos Souza",
        "email": "carlos.souza@example.com",
        "desired_role": "scrum_master",
        "status": "active",
        "availability": "afternoon",
        "phone": "(11) 92345-6789",
        "active": True,
        "registration_date": datetime.now()
    },
    {
        "id": 3,
        "name": "Ana Pereira",
        "email": "ana.pereira@example.com",
        "desired_role": "designer",
        "status": "inactive",
        "availability": "full_time",
        "phone": "(11) 93456-7890",
        "active": False,
        "registration_date": datetime.now()
    },
    {
        "id": 4,
        "name": "João Oliveira",
        "email": "joao.oliveira@example.com",
        "desired_role": "developer",
        "status": "active",
        "availability": "night",
        "phone": "(11) 94567-8901",
        "active": True,
        "registration_date": datetime.now()
    },
    {
        "id": 5,
        "name": "Patrícia Gomes",
        "email": "patricia.gomes@example.com",
        "desired_role": "analyst",
        "status": "active",
        "availability": "morning",
        "phone": "(11) 95678-9012",
        "active": True,
        "registration_date": datetime.now()
    }
]

latest_id = max(v["id"] for v in DATABASE)
CURRENT_ID = latest_id


def get_all_volunteers(filters: VolunteerFilters) -> List[VolunteerResponse]:
    result = DATABASE.copy()

    
    if filters.desired_role:
        result = [
            v for v in result 
            if v["desired_role"] == filters.desired_role.value
        ]

    if filters.availability:
        result = [
            v for v in result
            if v["availability"] == filters.availability.value
        ]

    if filters.status:
        result = [
            v for v in result
            if v["status"] == filters.status.value
        ]

    return [VolunteerResponse(**v) for v in result]


def get_volunteer_by_id(volunteer_id: int) -> VolunteerResponse:
    for v in DATABASE:
        if v["id"] == volunteer_id:
            return VolunteerResponse(**v)

    # Se não encontrar, lança 404
    raise HTTPException(status_code=404, detail="Voluntário não encontrado.")


def create_volunteer(data: VolunteerBase) -> VolunteerResponse:
   
    for v in DATABASE:
        if v["email"] == data.email:
            raise ValueError("E-mail já está cadastrado.")

    global CURRENT_ID
    CURRENT_ID += 1

    new_volunteer = {
        "id": CURRENT_ID,
        "name": data.name,
        "email": data.email,
        "phone": data.phone,
        "desired_role": data.desired_role.value,
        "availability": data.availability.value,
        "status": data.status.value,
        "registration_date": datetime.now(),
        "active": True
    }

    DATABASE.append(new_volunteer)

    return VolunteerResponse(**new_volunteer)
