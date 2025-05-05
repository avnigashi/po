# backend/Dockerfile
# Instructions to build the Docker image for the Flask backend service.
# (No changes from previous version)

# Start from an official Python base image (Debian-based)
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies:
# - openscad: The core requirement for rendering
# - build-essential, libpq-dev: Needed for building psycopg2 (PostgreSQL driver)
# - git: If you need to install dependencies from git repos
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openscad \
        build-essential \
        libpq-dev \
        # Add other system dependencies if needed (e.g., git)
    && \
    # Clean up apt cache to reduce image size
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the Flask app runs on (must match the port in the Flask app run command)
EXPOSE 5000

# Define the command to run the application
# Using flask run (requires FLASK_APP env var)
# Or use: CMD ["python", "backend_server.py"] if not using flask run
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
