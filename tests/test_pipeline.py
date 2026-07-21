import pipeline


def test_hello() -> None:
    assert pipeline.hello() == "Hello from pipeline!"
