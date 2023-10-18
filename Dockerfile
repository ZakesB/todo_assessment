FROM python:3.8-slim

# Install system dependencies for PostgreSQL and psycopg2
#RUN apt-get update && apt-get install -y \
#    postgresql-client \
#    libpq-dev
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip3 install psycopg2 \

WORKDIR /todo_server

COPY . /todo_server

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python3", "main.py"]
