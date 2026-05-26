# WE WORK REMOTELY

## OBSERVED BEHAVIOR
- allows basic unauthorized HTTP requests to get jobs data.
- response so far usually contains usable jobs-related business data.
- login-related response was unexpectedly observed during live integration testing.
    * THEREFORE: login response is now treated as real observable behavior, not only as artificial fixture coverage.

## AUTHORIZATION BEHAVIOR
- does not consistently require user authorization.
- login screen can appear in the initial response and should be treated as blocking factor when business data is absent/unusable.
- detector classifies login as blocking factor when it appears in the initial response and business data is absent/unusable.
    * STILL: login wall fixture remains in test coverage to reduce possibility of false-positive outcomes.

## ENDPOINT HANDLING
- endpoint is built from base URL + params and can be fetched directly from the URL line in the browser.

## TOOLS USED
- requests

## STABILITY OBSERVATIONS
- for the time written, the site mostly behaves consistently, but integration testing confirmed that login-related responses are possible.

## VERDICT
- this site is mostly stable, but login-related responses are possible.