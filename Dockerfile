# Use the official Python image as a base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY app.py /app
COPY requirements.txt /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
