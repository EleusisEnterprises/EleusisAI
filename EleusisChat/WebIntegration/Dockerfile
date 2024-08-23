# Dockerfile

# Base image
FROM python:3.10-slim

# Set environment variables
ENV SERPAPI_KEY=your_actual_serpapi_key_here

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "main.py"]
