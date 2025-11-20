from enum import Enum

class DesiredRoleEnum(str, Enum):
    developer = "desenvolvedor"
    designer = "designer"
    analyst = "analista"
    scrum_master = "scrum master"


class AvailabilityEnum(str, Enum):
    morning = "manhã"
    afternoon = "tarde"
    night = "noite"
    full_time = "tempo_integral"


class StatusEnum(str, Enum):
    active = "ativo"
    inactive = "inativo"
    pending = "pendente"