# REMOTE OK

## OBSERVED BEHAVIOR
- allows basic unauthorized HTTP requests to get jobs data.
- response so far contains usable jobs-related business data.

## AUTHORIZATION BEHAVIOR
- does not require user authorization.
- login screen is called directly from the UI, so it does not mess with the expected response type consistency.
- detector only classifies login as a blocking factor when it appears in the initial response and business data is absent/unusable.
    * STILL: added login wall fixture and used it in test coverage to reduce possibility of false-positive outcomes.

## ENDPOINT HANDLING
- endpoint is built from base URL + params and can be fetched directly from the URL line in the browser.

## TOOLS USED
- requests

## STABILITY OBSERVATIONS
- one of the site search params suddenly changed, which was quickly handled because integration tests detected regression in endpoint behavior.
- for the time written, unexpected behavior from that site does not appear further.

## VERDICT
- this site is stable and acceptable for future job scraping until proven otherwise.