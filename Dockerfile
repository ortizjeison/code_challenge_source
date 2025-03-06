# Use an official Selenium image with Chromium installed
FROM selenium/standalone-chrome:latest

# Switch to root for package installation
USER root

# Ensure logs appear immediately
ENV PYTHONUNBUFFERED=True

# Set working directory
ENV APP_HOME=/app
WORKDIR $APP_HOME
COPY . ./

# Install Python, virtual environment tools, and Chromium browser
RUN apt-get update && apt-get install -y python3 python3-venv python3-pip chromium-browser chromium-driver && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create a virtual environment for Python packages
RUN python3 -m venv /venv

# Activate the virtual environment
ENV PATH="/venv/bin:$PATH"

# Install Python dependencies inside the virtual environment
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Switch back to the Selenium user for security
#USER seluser

# Set a default port
ENV PORT=8080

# Run the app with Gunicorn, using the virtual environment
CMD ["/venv/bin/gunicorn", "--bind", ":8080", "--workers", "1", "--threads", "8", "--timeout", "0", "app:app"]
