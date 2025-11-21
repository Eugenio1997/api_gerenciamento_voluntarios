from datetime import datetime
from typing import Dict, List

from fastapi import HTTPException
from app.schemas.enums import StatusEnum
from app.schemas.volunteer import VolunteerBase, VolunteerResponse
from app.utils.filters import VolunteerFilters

DATABASE: List[Dict] = [
    {
        "id": 1,
        "name": "Maria Silva",
        "email": "maria.silva@example.com",
        "desired_role": "analista",
        "status": "ativo",
        "availability": "manhã",
        "phone": "(11) 91234-5678",
        "active": True,
        "registration_date": datetime.now()
    },
    {
        "id": 2,
        "name": "Carlos Souza",
        "email": "carlos.souza@example.com",
        "desired_role": "scrum_master",
        "status": "ativo",
        "availability": "tarde",
        "phone": "(11) 92345-6789",
        "active": True,
        "registration_date": datetime.now()
    },
    {
        "id": 3,
        "name": "Ana Pereira",
        "email": "ana.pereira@example.com",
        "desired_role": "designer",
        "status": "inativo",
        "availability": "tempo_integral",
        "phone": "(11) 93456-7890",
        "active": False,
        "registration_date": datetime.now()
    },
    {
        "id": 4,
        "name": "João Oliveira",
        "email": "joao.oliveira@example.com",
        "desired_role": "desenvolvedor",
        "status": "ativo",
        "availability": "noite",
        "phone": "(11) 94567-8901",
        "active": True,
        "registration_date": datetime.now()
    },
    {
        "id": 5,
        "name": "Patrícia Gomes",
        "email": "patricia.gomes@example.com",
        "desired_role": "analista",
        "status": "ativo",
        "availability": "manhã",
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
        "desired_role": data.desired_role,
        "availability": data.availability,
        "status": data.status,
        "registration_date": datetime.now(),
        "active": True
    }

    DATABASE.append(new_volunteer)

    return VolunteerResponse(**new_volunteer)


def update_volunteer(volunteer_id: int, data: VolunteerBase) -> VolunteerResponse:
    for index, v in enumerate(DATABASE):
        if v["id"] == volunteer_id:

            for other in DATABASE:
                if other["email"] == data.email and other["id"] != volunteer_id:
                    raise HTTPException(status_code=409, detail="E-mail já está cadastrado por outro voluntário.")

            updated_volunteer = {
                "id": volunteer_id,
                "name": data.name,
                "email": data.email,
                "phone": data.phone,
                "desired_role": data.desired_role,
                "availability": data.availability,
                "status": data.status,
                "registration_date": v["registration_date"],
                "active": v["active"]
            }

            DATABASE[index] = updated_volunteer
            return VolunteerResponse(**updated_volunteer)

    raise HTTPException(status_code=404, detail="Voluntário não encontrado.")


def delete_volunteer(volunteer_id: int) -> None:
    for v in DATABASE:
        if v["id"] == volunteer_id:
            v["status"] = StatusEnum.inactive.value
            return

    raise HTTPException(status_code=404, detail="Voluntário não encontrado.")
