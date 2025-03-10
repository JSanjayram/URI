# Use a slim Python image as the base
FROM python:3.9-slim

# Install necessary system dependencies, including Chromium and ChromeDriver
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    chromium \
    chromium-driver \
    libnss3 \
    libgconf-2-4 \
    && apt-get clean

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY . .

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Start the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
