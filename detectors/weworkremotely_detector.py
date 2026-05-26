from detectors.core_detector import (
    DetectionResult,
    ResponseType,
)
from helpers.helpers import (
    count_present_markers,
    marker_repeats_at_least,
)


WEWORKREMOTELY_STRONG_LOGIN_MARKERS = [
    'class="auth-redirect',
    'crossorigin="anonymous',
]

WEWORKREMOTELY_STRONG_JOB_MARKERS = [
    'class=" new-listing',
    'class="new-listing',
]

# Observed but not always used by current classifier logic.
WEWORKREMOTELY_SUPPORTING_LOGIN_MARKERS = [
    'auth-box-size',
    'id="sign-in',
    'href="/account/sign_in',
]

WEWORKREMOTELY_SUPPORTING_JOB_MARKERS = [
    'id="job-listings',
    'class="jobs',
]

WEWORKREMOTELY_WEAK_LOGIN_MARKERS = [
    "sign in",
    "login",
]


def classify_weworkremotely_response(text: str) -> DetectionResult:

    result = detect_login_screen_on_weworkremotely(text)

    if result:
        return result

    result = detect_weworkremotely_jobs(text)

    if result:
        return result

    return DetectionResult(
        ResponseType.UNKNOWN,
        "need manual investigation",
    )

def detect_weworkremotely_jobs(text: str) -> DetectionResult | None:
    minimum_expected_matches = 1

    if marker_repeats_at_least(text, WEWORKREMOTELY_STRONG_JOB_MARKERS, minimum_expected_matches):
        return DetectionResult(
            ResponseType.JOB_FOUND,
            "job applications found",
        )

def detect_login_screen_on_weworkremotely(text: str) -> DetectionResult | None:
    minimum_expected_matches = 1

    matches = count_present_markers(text, WEWORKREMOTELY_STRONG_LOGIN_MARKERS)

    if minimum_expected_matches <= matches:
        return DetectionResult(
            ResponseType.REQUIRED_LOGIN,
            "redirected to login screen",
        )
