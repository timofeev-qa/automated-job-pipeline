# GLASSDOOR

## OBSERVED BEHAVIOR
- allows basic unauthorized HTTP requests to get jobs data.
- response so far contains usable jobs-related business data.

## AUTHORIZATION BEHAVIOR
- does not require user authorization.
- login screen is called directly from the UI, so it does not mess with the expected response type consistency.
- detector only classifies login as a blocking factor when it appears in the initial response and business data is absent/unusable.
    * CHANGED: all `glassdoor_strong_login_markers` are transferred to supporting markers.

## ENDPOINT HANDLING
- endpoint is currently represented as a full browser-observed URL and can be requested directly.
- initially discovered through browser document request inspection.
- later rechecked and confirmed as directly reachable through a normal HTTP request.

## TOOLS USED
- requests

## STABILITY OBSERVATIONS
- for the time written, unexpected behavior from that site does not appear.

## VERDICT
- this site is stable and acceptable for future job scraping until proven otherwise.