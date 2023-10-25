FROM python:3.11-buster as builder

RUN python -m venv /venv
RUN . /venv/bin/activate && pip install poetry==1.6.1

ENV POETRY_NO_INTERACTION=1 \
	POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=$POETRY_CACHE_DIR . /venv/bin/activate && poetry install --no-root

FROM python:3.11-slim-buster as runtime

ENV VIRTUAL_ENV=/venv \
	PATH="/venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR /app

COPY . ./

EXPOSE 8000
