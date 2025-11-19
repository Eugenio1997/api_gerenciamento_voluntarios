from typing import Dict, List
from app.schemas.volunteer import VolunteerResponse
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
        "active": True
    },
    {
        "id": 2,
        "name": "Carlos Souza",
        "email": "carlos.souza@example.com",
        "desired_role": "scrum_master",
        "status": "active",
        "availability": "afternoon",
        "phone": "(11) 92345-6789",
        "active": True
    },
    {
        "id": 3,
        "name": "Ana Pereira",
        "email": "ana.pereira@example.com",
        "desired_role": "designer",
        "status": "inactive",
        "availability": "full_time",
        "phone": "(11) 93456-7890",
        "active": False  # soft delete
    },
    {
        "id": 4,
        "name": "João Oliveira",
        "email": "joao.oliveira@example.com",
        "desired_role": "developer",
        "status": "active",
        "availability": "night",
        "phone": "(11) 94567-8901",
        "active": True
    },
    {
        "id": 5,
        "name": "Patrícia Gomes",
        "email": "patricia.gomes@example.com",
        "desired_role": "analyst",
        "status": "active",
        "availability": "morning",
        "phone": "(11) 95678-9012",
        "active": True
    }
]


CURRENT_ID = 1


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