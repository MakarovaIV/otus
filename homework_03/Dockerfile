# How to build and run containder:
# $ cd homework_03
# $ docker build ./ -t homework03:1
# $ docker run -it -p 8000:8000 homework03:1

FROM python:3.10.8-bullseye

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN pip install --upgrade pip && \
    pip install poetry==1.2.2

RUN poetry config virtualenvs.create false --local

COPY pyproject.toml poetry.lock ./

RUN poetry install --only main

COPY . .

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000
EXPOSE 8000/tcp