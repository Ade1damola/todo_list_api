FROM python:alpine3.17

WORKDIR /main

COPY . .

CMD ["python3", "app.py"]