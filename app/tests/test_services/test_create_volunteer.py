from app.schemas.volunteer import VolunteerBase
from app.services.volunteer_service import create_volunteer


def test_create_volunteer():

    new_v = {
        "name": "Carlos Souza",
        "email": "carlos.souza@example.com",
        "desired_role": "scrum_master",
        "status": "active",
        "availability": "afternoon",
        "phone": "(11) 92345-6789",
        "active": True
    }

    v_created = create_volunteer(VolunteerBase(**new_v))
    assert v_created["name"] == new_v["name"]