# Build stage
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

ENV UV_EXTRA_INDEX_URL=https://download.pytorch.org/whl/cpu
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

WORKDIR /app

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
	--mount=type=bind,source=uv.lock,target=uv.lock \
	--mount=type=bind,source=pyproject.toml,target=pyproject.toml \
	uv sync --frozen --no-install-project --no-dev

# Copy the rest of the application
ADD . /app

# Install the project and its dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
	uv sync --frozen --no-dev

# Final stage
FROM python:3.12-slim-bookworm

# Copy the application from the builder
COPY --from=builder --chown=app:app /app /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Set the working directory
WORKDIR /app