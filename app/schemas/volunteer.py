from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from enum import Enum


class VolunteerBase(BaseModel):
    name: str = Field(
        ...,
        alias="nome",
        description="Nome completo do voluntário"
    )

    email: EmailStr = Field(
        ...,
        alias="email",
        description="E-mail do voluntário"
    )

    phone: str = Field(
        ...,
        alias="telefone",
        description="Telefone do voluntário"
    )

    desired_role: str = Field(
        ...,
        alias="funcao_desejada",
        description="Função desejada pelo voluntário"
    )

    availability: str = Field(
        ...,
        alias="disponibilidade",
        description="Disponibilidade do voluntário"
    )

    status: str = Field(
        ...,
        alias="status",
        description="Status atual do voluntário"
    )

    model_config = {
        "populate_by_name": True
    }


class VolunteerResponse(VolunteerBase):
    id: int = Field(
        ...,
        alias="id",
        description="Identificador único do voluntário"
    )

    registration_date: datetime = Field(
        ...,
        alias="data_registro",
        description="Data de registro do voluntário"
    )