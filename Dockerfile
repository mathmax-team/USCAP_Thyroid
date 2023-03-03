# syntax=docker/dockerfile:1

FROM python:3.10.10

WORKDIR /python-docker

COPY shortrequire.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]