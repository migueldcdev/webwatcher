FROM python:3.12-slim

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY src ./src
RUN uv sync --frozen --no-dev

CMD ["uv", "run", "python", "-c", "import pipeline; print(pipeline.hello())"]
