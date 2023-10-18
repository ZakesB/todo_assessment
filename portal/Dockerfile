FROM python:3.8-slim

WORKDIR /todo_server/portal

COPY . /todo_server/portal

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python3", "app.py"]
