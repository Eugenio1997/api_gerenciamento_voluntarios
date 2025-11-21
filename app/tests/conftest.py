import pytest
from datetime import datetime
from app.services.volunteer_service import DATABASE

@pytest.fixture(autouse=True)
def reset_database():
    DATABASE.clear()
    DATABASE.extend([
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
    ])
