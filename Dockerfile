FROM python:3.11.6

WORKDIR /bot

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .