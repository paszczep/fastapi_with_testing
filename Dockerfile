FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src/
COPY ./data /app/data/
COPY ./test /app/test/

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "80"]