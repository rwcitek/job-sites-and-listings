# Use an official Python runtime as a parent image, compatible with the Playwright version
FROM python:3.12-bookworm

# Set the working directory in the container
WORKDIR /app

# Install dependencies required for Playwright
# Note: The playwright package itself will be installed via pip
RUN apt-get update && apt-get install -y \
    wget \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
# Include playwright and any other dependencies your application requires
RUN pip install playwright==1.41.2 && playwright install --with-deps

# Add a user for running applications
RUN groupadd -r pwuser && useradd -r -g pwuser -G audio,video pwuser \
    && mkdir -p /home/pwuser && chown -R pwuser:pwuser /home/pwuser

# Use the created user
USER pwuser

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "scraper.py"]
