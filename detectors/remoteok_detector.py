from detectors.core_detector import (
    DetectionResult,
    ResponseType,
)
from helpers.helpers import (
    count_present_markers,
    marker_repeats_at_least,
)


REMOTEOK_STRONG_LOGIN_MARKERS = [
    'class="username_or_email',
    'class="action-login',
    'class="login-with',
    'href="/sign-up',
]

REMOTEOK_STRONG_JOB_MARKERS = [
    'class="job',
    'itemprop="hiringOrganization',
]

# Observed but not always used by current classifier logic.
REMOTEOK_SUPPORTING_LOGIN_MARKERS = [
    'by logging in you agree',
    'continue with email',
    'action-log-in',
    'href="/login',
]

REMOTEOK_SUPPORTING_JOB_MARKERS = [
    'class="company',
]

REMOTEOK_WEAK_LOGIN_MARKERS = [
    "sign in",
    "log in",
    "login",
    'not a member yet',
]


def classify_remoteok_response(text: str) -> DetectionResult:

    result = detect_login_screen_on_remoteok(text)

    if result:
        return result

    result = detect_remoteok_jobs(text)

    if result:
        return result

    return DetectionResult(
        ResponseType.UNKNOWN,
        "need manual investigation",
    )

def detect_remoteok_jobs(text: str) -> DetectionResult | None:
    minimum_expected_matches = 3

    if marker_repeats_at_least(text, REMOTEOK_STRONG_JOB_MARKERS, minimum_expected_matches):
        return DetectionResult(
            ResponseType.JOB_FOUND,
            "job applications found",
        )

def detect_login_screen_on_remoteok(text: str) -> DetectionResult | None:
    minimum_expected_matches = 1

    matches = count_present_markers(text, REMOTEOK_STRONG_LOGIN_MARKERS)

    if minimum_expected_matches <= matches:
        return DetectionResult(
            ResponseType.REQUIRED_LOGIN,
            "redirected to login screen",
        )
