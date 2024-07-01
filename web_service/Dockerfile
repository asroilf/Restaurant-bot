FROM python:latest

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
USER 1001

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

