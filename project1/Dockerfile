FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create log directory
RUN mkdir -p /var/log/django && chmod -R 777 /var/log/django

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run Django using Gunicorn (logs to stdout)
CMD ["gunicorn", "project1.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=3", "--log-level=info", "--access-logfile=-", "--error-logfile=-"]
