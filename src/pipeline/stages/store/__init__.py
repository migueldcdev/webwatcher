from services.db import save_snapshot


def run(url: str, content: str, summary: str) -> None:
    save_snapshot(url, content, summary)
