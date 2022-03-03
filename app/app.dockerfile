FROM python:3.8
LABEL author="Erick Brunoro"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "./src/main.py" ]