FROM python:alpine3.17

WORKDIR /main

COPY . /main

CMD ["python", "app.py"]