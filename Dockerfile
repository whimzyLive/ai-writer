FROM python:3-slim

ADD . /app
WORKDIR /app

ENV inputFile="./nextjs/fundamentals.md"
ENV outputDir="./.tmp"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ./src/main.py --input_file $inputFile --output_dir $outputDir