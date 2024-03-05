# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# Install system dependencies required by Playwright
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
# Note: Make sure to update these commands according to your application's specific dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and browsers
RUN pip install playwright
RUN playwright install

# Copy the rest of your application's code
COPY . /app

# Command to run on container start (for example, to start a Flask app)
# Replace the command below with your own command
CMD ["python", "your_app.py"]



COPY .devcontainer/install-doctl.sh /tmp/install-doctl.sh
RUN chmod +x /tmp/install-doctl.sh && /tmp/install-doctl.sh && rm /tmp/install-doctl.sh

# Start with a Python image.
FROM mcr.microsoft.com/playwright/python:v1.17.0-focal

# Set the working directory in the container
WORKDIR /app

# Copy the Python dependencies file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install the necessary browsers
RUN playwright install

# Copy the rest of your application's code
COPY . .

# Command to run on container start
CMD ["python", "./scraper.py"]
