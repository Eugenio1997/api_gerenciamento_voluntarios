from enum import Enum


class DesiredRoleEnum(str, Enum):
    developer = "developer"
    designer = "designer"
    analyst = "analyst"
    scrum_master = "scrum_master"


class AvailabilityEnum(str, Enum):
    morning = "morning"
    afternoon = "afternoon"
    night = "night"
    full_time = "full_time"


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    pending = "pending"
