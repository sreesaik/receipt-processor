
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the files
COPY . /app

# Install dependencies
RUN pip install flask

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "receipt.py"]