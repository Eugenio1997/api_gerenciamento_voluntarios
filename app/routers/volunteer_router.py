from fastapi import APIRouter, Depends, Path
from typing import List
from app.schemas.volunteer import VolunteerBase, VolunteerResponse
from app.utils.filters import VolunteerFilters
from app.services.volunteer_service import (
    get_all_volunteers,
    get_volunteer_by_id,
    create_volunteer,
    update_volunteer,
    delete_volunteer
)

router = APIRouter(
    prefix="/voluntarios",
    tags=["Voluntários"]
)

@router.get(
    "/",
    response_model=List[VolunteerResponse],
    summary="Listar voluntários",
    description="Retorna a lista de voluntários cadastrados com filtros opcionais."
)
def list_volunteers_endpoint(filters: VolunteerFilters = Depends()):
    return get_all_volunteers(filters)


@router.get(
    "/{voluntario_id}",
    response_model=VolunteerResponse,
    summary="Buscar voluntário",
    description="Retorna os dados de um voluntário específico."
)
def get_volunteer_by_id_endpoint(
    voluntario_id: int = Path(
        ...,
        description="ID do voluntário que deseja consultar."
    )
):
    return get_volunteer_by_id(voluntario_id)


@router.post(
    "/",
    response_model=VolunteerResponse,
    status_code=201,
    summary="Cadastrar voluntário",
    description="Cria um novo voluntário no sistema."
)
def add_volunteer_endpoint(data: VolunteerBase):
    return create_volunteer(data)


@router.put(
    "/{voluntario_id}",
    summary="Atualizar voluntário",
    description="Atualiza os dados de um voluntário existente."
)
def update_volunteer_endpoint(
    voluntario_id: int = Path(
        ...,
        description="ID do voluntário que deseja atualizar."
    ),
    data: VolunteerBase = ...
):
    return update_volunteer(voluntario_id, data)


@router.delete(
    "/{voluntario_id}",
    status_code=204,
    summary="Excluir voluntário",
    description="Remove um voluntário do sistema."
)
def delete_volunteer_endpoint(
    voluntario_id: int = Path(
        ...,
        description="ID do voluntário que será removido do sistema."
    )
):
    return delete_volunteer(voluntario_id)
