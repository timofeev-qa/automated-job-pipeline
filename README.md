# Automated Job Pipeline

Backend/API-oriented QA project for validating whether external job-board responses are business-usable before parsing.

Main idea:

> HTTP success does not guarantee business usability.

A response can return `200 OK` and still be unusable because of login walls, challenge pages, captcha screens, empty shells, or unstable external behavior.

## What this project tests

The project classifies job-board responses into known response types:

- `JOB_FOUND`
- `REQUIRED_LOGIN`
- `CHALLENGE_FOUND`
- `UNKNOWN`

The goal is not to bypass protections or scrape at any cost.
The goal is to observe real response behavior and decide whether a source is stable enough for future automation.

## Covered sources

- RemoteOK
- We Work Remotely
- Glassdoor
- Wellfound

## Key behavior examples

### Stable job response

Some sites return usable job data through a basic unauthorized HTTP request.

### Login-related response

Some responses may contain or return login-related pages. These are treated as blocking only when business data is absent or unusable.

### Challenge / captcha response

Wellfound showed unstable behavior across `requests`, `requests.Session`, `httpx`, and `Playwright`. Because the response was not stable enough, it was excluded as a reliable future source for now.

## Project structure

```text
clients/                 HTTP clients for each source
detectors/               Response classifiers
tests/fixtures/responses Sanitized deterministic response fixtures
tests/                   Unit and integration tests
docs/investigations/     Site behavior notes
helpers/                 Shared helper functions
```

## Tests
Run unit tests:
```pytest -m unit```

Run integration tests:
```pytest -m integration```

Repeat unit tests for stability check:
```pytest -m unit --count=100```

## Docker
Build image:
```docker build -t automated-job-pipeline .```

Run unit tests in Docker:
```docker run --rm automated-job-pipeline```

Run integration tests in Docker:
```docker run --rm automated-job-pipeline pytest -m integration```

### Notes
Integration tests depend on live third-party websites.
They are used to observe and classify live behavior, not to guarantee that external systems stay stable forever.

Deterministic behavior is tested through sanitized fixtures.