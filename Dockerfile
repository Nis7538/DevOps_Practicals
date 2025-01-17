FROM python:3.9-slim

WORKDIR /app

COPY . /app

EXPOSE 8000

CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "8000"]