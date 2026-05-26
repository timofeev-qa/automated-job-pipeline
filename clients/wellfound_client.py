import requests
import httpx
from playwright.sync_api import sync_playwright


class WellfoundClient:

    def __init__(self):
        self.base_url = "https://wellfound.com/role/qa-engineer"
        self.timeout = 10000

    def cli_get_response_with_requests(self, **override) -> requests.Response:
        response = requests.get(
            url = override.get(
                "url",
                self.base_url,
            ),
            headers={
                "User-Agent": "qa-response-classifier/0.1",
            },
            timeout=self.timeout,
        )

        return response

    def cli_get_response_with_session(self, **override) -> requests.Response:
        session = requests.Session()

        response = session.get(
            url = override.get(
                "url",
                self.base_url,
            ),
            headers={
                "User-Agent": "qa-response-classifier/0.1",
            },
            timeout=self.timeout,
        )

        session.close()

        return response

    def cli_get_response_with_httpx_sync(self, **override) -> httpx.Response:
        response = httpx.get(
            url = override.get(
                "url",
                self.base_url,
            ),
            headers={
                "User-Agent": "qa-response-classifier/0.1",
            },
            timeout=self.timeout,
        )

        return response

    def cli_get_response_with_playwright_sync(self, **override) -> tuple[int, str]:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)

            context = browser.new_context(
                user_agent="qa-response-classifier/0.1",
            )

            page = context.new_page()

            response = page.goto(
                url=override.get(
                    "url",
                    self.base_url,
                ),
                wait_until="networkidle",
                timeout=self.timeout
            )

            status = response.status if response else 0

            html = page.content()

            browser.close()

            return status, html