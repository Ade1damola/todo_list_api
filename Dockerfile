FROM python:alpine3.17

WORKDIR /app

COPY . /main

CMD ["python", "app.py"]