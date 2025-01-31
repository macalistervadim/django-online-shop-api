FROM python:3.12

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="$PATH:/root/.local/bin"

WORKDIR /app

RUN poetry config virtualenvs.create false

COPY backend/pyproject.toml backend/poetry.lock /app/

RUN poetry install --no-interaction --no-ansi --no-root

COPY ./backend/ /app/backend/

RUN poetry run python /app/backend/manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
