# Use an official Python image as the base image
FROM python:3.11.7-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Expose the port on which the app will run (match with Gunicorn binding)
EXPOSE 8080

# Run the application using Gunicorn, binding to port 8000
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8080"]
