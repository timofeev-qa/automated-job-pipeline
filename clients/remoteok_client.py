import requests


class RemoteokClient:

    def __init__(self):
        self.base_url = "https://remoteok.com/"
        self.timeout = 10

    def cli_get_response(self) -> requests.Response:
        response = requests.get(
            url=self.base_url,
            params={
                "tags": "quality assurance",
                "location": "Worldwide",
                "action": "get_jobs",
            },
            headers={
                "User-Agent": "qa-response-classifier/0.1",
            },
            timeout=self.timeout,
            )

        return response