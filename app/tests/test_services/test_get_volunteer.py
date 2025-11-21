from app.services.volunteer_service import get_volunteer_by_id

def test_get_volunteer_by_id():
    v = get_volunteer_by_id(1)
    assert v.id == 1
    assert v.name == "Maria Silva"
