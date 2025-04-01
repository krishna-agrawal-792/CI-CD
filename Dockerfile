# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY api /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose API port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
