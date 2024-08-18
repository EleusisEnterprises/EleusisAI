# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies globally (if necessary)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Create a virtual environment in /app/venv
RUN python -m venv /app/venv

# Install dependencies inside the virtual environment using the correct path
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Expose the port the application will run on
EXPOSE 6000
