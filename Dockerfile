FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install system dependencies needed for building some Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Use port 8080 for Cloud Run
EXPOSE 8080

# Run with gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "run:app"]
