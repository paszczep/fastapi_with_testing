FROM python:3.10-slim

WORKDIR /app

COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock

RUN pip install pipenv
# RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --no-cache-dir

COPY ./src /app/src
COPY ./data /app/data

CMD ["uvicorn", "src.api:app", "--reload"]