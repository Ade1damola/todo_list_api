FROM python:alpine3.17

WORKDIR /main

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "main.py"]