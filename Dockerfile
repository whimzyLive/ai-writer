FROM python:3-slim

COPY requirements.txt /requirements.txt
COPY entrypoint.sh /entrypoint.sh
COPY _template.md /_template.md
COPY src/ /src/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]