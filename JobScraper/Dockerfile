# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install pyppeteer dependencies
RUN apt-get update \
    && apt-get install -y wget \
    && apt-get install -y libxss1 \
    && apt-get install -y libappindicator1 \
    && apt-get install -y libindicator7 \
    && apt-get install -y libasound2 \
    && apt-get install -y libatk-bridge2.0-0 \
    && apt-get install -y libatspi2.0-0 \
    && apt-get install -y libdrm2 \
    && apt-get install -y libgbm1 \
    && apt-get install -y libgtk-3-0 \
    && apt-get install -y libnspr4 \
    && apt-get install -y libnss3 \
    && apt-get install -y libx11-xcb1 \
    && apt-get install -y libxcomposite1 \
    && apt-get install -y libxdamage1 \
    && apt-get install -y libxrandr2 \
    && apt-get clean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Copy the content of the local src directory to the working directory
COPY . .

# Command to run on container start
CMD [ "python", "./scraper.py" ]
