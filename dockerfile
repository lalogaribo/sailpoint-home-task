FROM python:3.9-alpine

WORKDIR /app

RUN pip install --upgrade pip \
    && pip install requests tabulate

COPY . .

ENV GITHUB_TOKEN=${GITHUB_TOKEN}

CMD [ "python", "main.py" ]