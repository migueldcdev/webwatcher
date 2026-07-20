from services.llm_client import summarize_diff


def run(diff_text: str) -> str:
    return summarize_diff(diff_text)
