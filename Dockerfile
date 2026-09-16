# --------------------------------------------------
# BASE IMAGE
# --------------------------------------------------
FROM python:3.12-slim

# --------------------------------------------------
# INSTALL UV
# --------------------------------------------------
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# --------------------------------------------------
# WORK DIRECTORY
# --------------------------------------------------
WORKDIR /app

# --------------------------------------------------
# DEPENDENCIES
# --------------------------------------------------
# Primero copiamos únicamente los archivos de dependencias.
# Esto ayuda a aprovechar el cache de Docker.
COPY pyproject.toml uv.lock* ./

# Instalamos dependencias.
# --no-dev evita instalar pytest y otras dependencias de desarrollo.
RUN uv sync --no-dev

# --------------------------------------------------
# APPLICATION CODE
# --------------------------------------------------
COPY app/ ./app/

# --------------------------------------------------
# PORT
# --------------------------------------------------
EXPOSE 8080

# --------------------------------------------------
# START APPLICATION
# --------------------------------------------------
CMD ["sh", "-c", "uv run uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}"]