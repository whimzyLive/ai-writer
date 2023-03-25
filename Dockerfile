FROM python:3-slim

COPY . /

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]