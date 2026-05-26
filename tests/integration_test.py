from detectors.core_detector import ResponseType
from detectors.remoteok_detector import classify_remoteok_response
from detectors.weworkremotely_detector import classify_weworkremotely_response
from detectors.glassdoor_detector import classify_glassdoor_response
from detectors.wellfound_detector import classify_wellfound_response

import pytest


@pytest.mark.integration
def test_success_classification_jobs_remoteok_response(remoteok_client):
    response = remoteok_client.cli_get_response()

    expected_status_code = 200

    assert expected_status_code == response.status_code

    result = classify_remoteok_response(response.text)

    assert result.response_type == ResponseType.JOB_FOUND
    assert result.reason == "job applications found"


@pytest.mark.integration
def test_success_classification_of_weworkremotely_response(weworkremotely_client):
    response = weworkremotely_client.cli_get_response()

    expected_status_codes = [
        200,
        403,
    ]

    assert response.status_code in expected_status_codes

    result = classify_weworkremotely_response(response.text)

    assert result.response_type in ResponseType
    assert result.response_type != ResponseType.UNKNOWN


@pytest.mark.integration
def test_success_classification_jobs_glassdoor_response(glassdoor_client):
    response = glassdoor_client.cli_get_response()

    expected_status_code = 200

    assert expected_status_code == response.status_code

    result = classify_glassdoor_response(response.text)

    assert result.response_type == ResponseType.JOB_FOUND
    assert result.reason == "job applications found"


@pytest.mark.integration
def test_success_classification_of_wellfound_response(wellfound_client):
    response = wellfound_client.cli_get_response_with_requests()

    expected_status_codes = [
        200,
        403,
    ]

    assert response.status_code in expected_status_codes

    result = classify_wellfound_response(response.text)

    assert result.response_type in ResponseType
    assert result.response_type != ResponseType.UNKNOWN