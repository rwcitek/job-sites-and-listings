# Start with the Playwright-provided Python image for compatibility with Playwright requirements.
FROM mcr.microsoft.com/playwright/python:v1.17.0-focal

# Set the working directory in the container to /app.
WORKDIR /app

# Prevent Python from generating .pyc files in the container.
ENV PYTHONDONTWRITEBYTECODE 1
# Prevent Python from buffering stdout and stderr.
ENV PYTHONUNBUFFERED 1

# Copy the Python dependencies file into the working directory.
COPY requirements.txt .

# Install Python dependencies from the requirements file.
RUN pip install --no-cache-dir -r requirements.txt

# Install the necessary browsers using Playwright.
RUN playwright install

# Optionally, include custom script installation (e.g., for DigitalOcean CLI tools).
# Ensure your install-doctl.sh script is in the .devcontainer directory of your repository.
COPY .devcontainer/install-doctl.sh /tmp/install-doctl.sh
RUN chmod +x /tmp/install-doctl.sh && /tmp/install-doctl.sh && rm /tmp/install-doctl.sh

# Copy the rest of your application's code into the container.
COPY . .

# Specify the command to run on container start. Update this command based on your entry script.
CMD ["python", "./scraper.py"]
