import pytest

from detectors.core_detector import ResponseType
from detectors.remoteok_detector import (
    classify_remoteok_response,
    detect_remoteok_jobs,
    detect_login_screen_on_remoteok,
)
from detectors.weworkremotely_detector import (
    classify_weworkremotely_response,
    detect_weworkremotely_jobs,
    detect_login_screen_on_weworkremotely,
)
from detectors.glassdoor_detector import (
    classify_glassdoor_response,
    detect_glassdoor_jobs,
)
from detectors.wellfound_detector import (
    classify_wellfound_response,
    detect_wellfound_jobs,
    detect_js_challenge_on_wellfound,
    detect_supporting_captcha_on_wellfound,
)
from helpers.helpers import load_fixture


@pytest.mark.unit
def test_remoteok_detector_catches_jobs_response():
    text = load_fixture("remoteok", "job_found.html")

    result = detect_remoteok_jobs(text)

    expected_result_type = ResponseType.JOB_FOUND
    expected_reason = "job applications found"

    assert expected_result_type == result.response_type
    assert expected_reason == result.reason

    assert not detect_login_screen_on_remoteok(text)
    assert result == classify_remoteok_response(text)


@pytest.mark.unit
def test_weworkremotely_detector_catches_jobs_response():
    text = load_fixture("weworkremotely", "job_found.html")

    result = detect_weworkremotely_jobs(text)

    expected_result_type = ResponseType.JOB_FOUND
    expected_reason = "job applications found"

    assert expected_result_type == result.response_type
    assert expected_reason == result.reason

    assert not detect_login_screen_on_weworkremotely(text)
    assert result == classify_weworkremotely_response(text)


@pytest.mark.unit
def test_glassdoor_detector_catches_jobs_response():
    text = load_fixture("glassdoor", "job_found.html")

    result = detect_glassdoor_jobs(text)

    expected_result_type = ResponseType.JOB_FOUND
    expected_reason = "job applications found"

    assert expected_result_type == result.response_type
    assert expected_reason == result.reason

    assert result == classify_glassdoor_response(text)


@pytest.mark.unit
def test_wellfound_detector_catches_jobs_response():
    text = load_fixture("wellfound", "job_found.html")

    result = detect_wellfound_jobs(text)

    expected_result_type = ResponseType.JOB_FOUND
    expected_reason = "job applications found"

    assert expected_result_type == result.response_type
    assert expected_reason == result.reason

    assert not detect_js_challenge_on_wellfound(text)
    assert result == classify_wellfound_response(text)


@pytest.mark.unit
def test_remoteok_detector_detects_login_required_page():
    text = load_fixture("remoteok", "login_required.html")

    result = detect_login_screen_on_remoteok(text)

    expected_result_type = ResponseType.REQUIRED_LOGIN
    expected_reason = "redirected to login screen"

    assert expected_result_type == result.response_type
    assert expected_reason == result.reason

    assert not detect_remoteok_jobs(text)


@pytest.mark.unit
def test_weworkremotely_detector_detects_login_required_page():
    text = load_fixture("weworkremotely", "login_required.html")

    result = detect_login_screen_on_weworkremotely(text)

    expected_result_type = ResponseType.REQUIRED_LOGIN
    expected_reason = "redirected to login screen"

    assert expected_result_type == result.response_type
    assert expected_reason == result.reason

    assert not detect_weworkremotely_jobs(text)


@pytest.mark.unit
def test_wellfound_detector_detects_challenge_response():
    text = load_fixture("wellfound", "challenge_required.html")

    result = detect_js_challenge_on_wellfound(text)

    expected_result_type = ResponseType.CHALLENGE_FOUND
    expected_reason = "js enabled and cookies required"

    assert expected_result_type == result.response_type
    assert expected_reason == result.reason

    assert not detect_wellfound_jobs(text)
    assert result == classify_wellfound_response(text)


@pytest.mark.unit
def test_wellfound_detector_detects_captcha_response():
    text = load_fixture("wellfound", "captcha_required.html")

    result = detect_supporting_captcha_on_wellfound(text)

    expected_result_type = ResponseType.CHALLENGE_FOUND
    expected_reason = "captcha completion required"

    assert expected_result_type == result.response_type
    assert expected_reason == result.reason

    assert not detect_wellfound_jobs(text)
    assert result == classify_wellfound_response(text)