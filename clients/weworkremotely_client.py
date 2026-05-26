import requests


class WeworkremotelyClient:

    def __init__(self):
        self.base_url = "https://weworkremotely.com/remote-jobs/search"
        self.timeout = 10

    def cli_get_response(self) -> requests.Response:
        response = requests.get(
            url=self.base_url,
            params={
                "search_uuid": "",
                "sort": "",
                "term": "QA",
                "categories_chosen": "",
                "countries_chosen": "",
                "chosen-salary_range": "",
                "skills_chosen": "",
            },
            headers={
                "User-Agent": "qa-response-classifier/0.1",
            },
            timeout=self.timeout
        )

        return response