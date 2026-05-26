from detectors.core_detector import (
    DetectionResult,
    ResponseType,
)
from helpers.helpers import (
    count_present_markers,
    marker_repeats_at_least,
)


WELLFOUND_STRONG_JOB_MARKERS = [
    'testid="startup-head',
    'href="/company',
]

WELLFOUND_STRONG_CHALLENGE_MARKERS = [
    'challenge-error-title',
    'challenge-error-text',
    'challenge-platform',
]

WELLFOUND_SUPPORTING_CAPTCHA_MARKERS = [
    'geo.captcha-delivery',
    'ct.captcha-delivery',
    'DataDome CAPTCHA',
]

# Observed but not always used by current classifier logic.
WELLFOUND_STRONG_CAPTCHA_MARKERS = [
]

WELLFOUND_SUPPORTING_CHALLENGE_MARKERS = [
    'enable javascript and cookies',
    'enable js and disable any',
]

WELLFOUND_SUPPORTING_JOB_MARKERS = [
    'button">Save',
    'href=/jobs/',
    'button">Apply',
]

WELLFOUND_WEAK_CHALLENGE_MARKERS = [
    'javascript',
    'cookies',
    'cloudflare',
    'cf',
]


def classify_wellfound_response(text: str) -> DetectionResult:

    result = detect_strong_captcha_on_wellfound(text)

    if result:
        return result

    result = detect_js_challenge_on_wellfound(text)

    if result:
        return result

    result = detect_wellfound_jobs(text)

    if result:
        return result

    potential_result = detect_supporting_captcha_on_wellfound(text)

    if potential_result and not result:
        return potential_result

    return DetectionResult(
        ResponseType.UNKNOWN,
        "need manual investigation",
    )

def detect_strong_captcha_on_wellfound(text: str) -> DetectionResult | None:
    minimum_expected_matches = 1

    matches = count_present_markers(text, WELLFOUND_STRONG_CAPTCHA_MARKERS)

    if minimum_expected_matches <= matches:
        return DetectionResult(
            ResponseType.CHALLENGE_FOUND,
            "captcha completion required",
        )

def detect_supporting_captcha_on_wellfound(text: str) -> DetectionResult | None:
    minimum_expected_matches = 1

    matches = count_present_markers(text, WELLFOUND_SUPPORTING_CAPTCHA_MARKERS)

    if minimum_expected_matches <= matches:
        return DetectionResult(
            ResponseType.CHALLENGE_FOUND,
            "captcha completion required",
        )

def detect_wellfound_jobs(text: str) -> DetectionResult | None:
    minimum_expected_matches = 3

    if marker_repeats_at_least(text, WELLFOUND_STRONG_JOB_MARKERS, minimum_expected_matches):
        return DetectionResult(
            ResponseType.JOB_FOUND,
            "job applications found",
        )

def detect_js_challenge_on_wellfound(text: str) -> DetectionResult | None:
    minimum_expected_matches = 1

    matches = count_present_markers(text, WELLFOUND_STRONG_CHALLENGE_MARKERS)

    if minimum_expected_matches <= matches:
        return DetectionResult(
            ResponseType.CHALLENGE_FOUND,
            "js enabled and cookies required",
        )