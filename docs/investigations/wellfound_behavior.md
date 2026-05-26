# WELLFOUND

## OBSERVED BEHAVIOR
- does not consistently respond with jobs data. Most of the time responds with "challenge".
    * ALSO: does not consistently respond with unauthorized challenge. Sometimes (as discovered once at some not-recorded time period) just gives valid job data for unauthorized client.
    * THEREFORE: this site cannot provide consistent response handling by the same client.

## AUTHORIZATION BEHAVIOR
- does not require user authorization.
    * STILL: sometimes expects client to complete challenge before giving access to the page content.
    * CONCEPT: my end-goal for this project is to reduce initial cost of site classification, not create additional complexity such as challenge completion or anti-bot evasion.
    * CONCEPT: I am observing real API behavior, not trying to manipulate or abuse it.
    * TRYING SOLUTIONS: requests -> Session -> httpx -> Playwright -> solution costs too much.

## ENDPOINT HANDLING
- endpoint is built directly from URL and can be fetched directly from browser URL line.

## TOOLS USED
- requests
- Session
- httpx
- Playwright

## STABILITY OBSERVATIONS
- for the time written, non-consistent results are common.

## VERDICT
- this site is not consistent and not acceptable for future job scraping until proven otherwise.