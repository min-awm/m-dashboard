FROM python:3.12-slim-trixie
FROM ghcr.io/astral-sh/uv:latest AS uv

WORKDIR /app
COPY --from=uv /uv /uvx /bin/

COPY . /app
RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]