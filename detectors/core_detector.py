from dataclasses import dataclass
from enum import Enum


# Observed but not always used by current classifier logic.
COMMON_WEAK_JOB_MARKERS = [
    "technical",
    "testing",
    "test",
    "qa",
    "junior",
    "middle",
    "mid",
    "senior",
    "master",
    "engineer",
    "position",
    "manual",
    "automation",
    "automated",
    "job",
    "jobs",
    "salary",
    "quality assurance",
    "software",
    "startup",
]

COMMON_WEAK_LOGIN_MARKERS = [
    "sign in",
    "login",
]


class ResponseType(str, Enum):
    CHALLENGE_FOUND = "challenge_found"
    REQUIRED_LOGIN = "required_login"
    JOB_FOUND = "job_found"
    UNKNOWN = "unknown"

@dataclass
class DetectionResult:
    response_type: ResponseType
    reason: str