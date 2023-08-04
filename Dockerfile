FROM python:3.9-slim

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip3 install --proxy="10.1.123.16:8888" -r requirements.txt --no-cache-dir

COPY ./app ./app

CMD [ "python", "./app/main.py" ]