from pathlib import Path


FIXTURES_DIR = Path("tests/fixtures/responses")


def load_fixture(site: str, filename: str) -> str:
    return (FIXTURES_DIR / site / filename).read_text(encoding="utf8")

def count_present_markers(text: str, markers: list[str]) -> int:
    matches = 0

    for marker in markers:
        if marker in text:
            matches += 1

    return matches

def marker_repeats_at_least(text: str, markers: list[str], minimum_count: int) -> bool:
    for marker in markers:
        if text.count(marker) >= minimum_count:
            return True

    return False