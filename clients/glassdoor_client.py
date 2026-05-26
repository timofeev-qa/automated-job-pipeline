import requests


class GlassdoorClient:

    def __init__(self):
        self.base_url = "https://www.glassdoor.com/Job/remote-us-qa-jobs-SRCH_IL.0,9_IS11047_KO10,12.htm"
        self.timeout = 10

    def cli_get_response(self) -> requests.Response:
        response = requests.get(
            url=self.base_url,
            headers={
                "User-Agent": "qa-response-classifier/0.1",
            },
            timeout=self.timeout
        )

        return response