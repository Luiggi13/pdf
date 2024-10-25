
FROM python:3.9
LABEL maintainer="Christian Llansola"

RUN apt-get update
RUN apt-get -y install ghostscript
RUN gs --help
RUN sleep 2

COPY . .

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt




CMD ["fastapi", "run", "main.py", "--port", "1313"]