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
