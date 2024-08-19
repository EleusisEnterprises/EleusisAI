# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr

# Set environment variables
ENV FLASK_ENV=production
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

# Make port 6000 available to the world outside this container
EXPOSE 6000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "main.py"]
