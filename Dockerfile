FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libssl1.1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p logs

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--certfile=/app/certs/cert.pem", "--keyfile=/app/certs/key.pem", "--workers", "4", "--access-logfile", "-", "--error-logfile", "-", "run:app"]
