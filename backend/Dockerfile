# Stage 1: lấy binary uv
FROM ghcr.io/astral-sh/uv:latest AS uv

# Stage 2: app chính
FROM python:3.12-slim-trixie AS app

WORKDIR /app

# copy binary từ stage uv
COPY --from=uv /uv /uvx /bin/

# copy code vào container
COPY . /app

# cài dependencies bằng uv
RUN uv sync

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
