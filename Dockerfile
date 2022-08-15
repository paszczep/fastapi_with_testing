FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt ./app/requirements.txt

RUN pip install -r ./app/requirements.txt

COPY ./src /app/src
COPY ./data /app/data

CMD ["uvicorn", "src.api:app", "--reload"]