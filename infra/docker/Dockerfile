# Stage 1: Build
FROM python:3.12-slim as builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl git gettext && \
    rm -rf /var/lib/apt/lists/*

RUN msguniq --version

RUN pip install --no-cache-dir uv

COPY ../../pyproject.toml /app/

RUN uv venv /app/.venv && \
    uv pip install ".[dev]"

# Stage 2: Production
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends locales gettext && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir uv

COPY --from=builder /app/.venv /app/.venv
COPY ../.. /app/

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uv", "run", "gunicorn", "backend.config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]
