from detectors.core_detector import (
    DetectionResult,
    ResponseType,
)
from helpers.helpers import (
    marker_repeats_at_least,
)


GLASSDOOR_STRONG_JOB_MARKERS = [
    'test="job-card',
    'test="job-title',
    'id="job-employer',
    'jobcard_savebuttoncontainer',
]

# Observed but not always used by current classifier logic.
GLASSDOOR_STRONG_LOGIN_MARKERS = [
]

GLASSDOOR_SUPPORTING_LOGIN_MARKERS = [
    'label="sign in',
    'test="auth-entry',
    'name="email-input',
]

GLASSDOOR_SUPPORTING_JOB_MARKERS = [
    'class="job',
    'class="jobs',
    'joblistitem',
    'test="detailsalary',
    'class="employer',
]

GLASSDOOR_WEAK_LOGIN_MARKERS = [
    "sign in",
]


def classify_glassdoor_response(text: str) -> DetectionResult:
    result = detect_glassdoor_jobs(text)

    if result:
        return result

    return DetectionResult(
        ResponseType.UNKNOWN,
        "need manual investigation",
    )

def detect_glassdoor_jobs(text: str) -> DetectionResult | None:
    minimum_expected_matches = 3

    if marker_repeats_at_least(text, GLASSDOOR_STRONG_JOB_MARKERS, minimum_expected_matches):
        return DetectionResult(
            ResponseType.JOB_FOUND,
            "job applications found",
        )
