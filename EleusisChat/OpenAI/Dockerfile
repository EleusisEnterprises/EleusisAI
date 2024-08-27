# Use an official Python runtime as a parent image
FROM python:3.10-slim

#Pass Python Root
ENV PYTHONPATH=.EleusisChat/
ENV PYTHONPATH=.EleusisChat\OpenAI\tools/

# Set environment variables
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

# Set the working directory in the container
WORKDIR /app

# Copy all necessary files, including main.py, to the /app directory
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run main.py when the container launches
CMD ["python", "main.py"]
