FROM python:3-slim

COPY . /app
WORKDIR /app

RUN ls -la

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/app/entrypoint.sh"]