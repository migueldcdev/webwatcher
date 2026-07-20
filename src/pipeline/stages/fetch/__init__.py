from services.http_client import fetch_url


def run(url: str) -> str:
    return fetch_url(url)
