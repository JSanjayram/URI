FROM python:3.9-slim

# Install Chromium and ChromeDriver
RUN apt-get update && apt-get install -y chromium chromium-driver
RUN chromium-browser --version && chromedriver --version

# Set the working directory
WORKDIR /app

# Copy application files
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the Flask app's port
EXPOSE 5000
which chromedriver

# Start the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
RUN wget https://chromedriver.storage.googleapis.com/<VERSION>/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver
