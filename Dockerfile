# Base Docker image Official Python 3.12
FROM python:3.12

# Set 'build-time' environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Extra packages required for Material for MkDocs plugins
RUN apt-get update && \
    apt-get install -y git python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add requirements
COPY requirements.txt /app/requirements.txt

# Set working directory for requirements installation
WORKDIR /app/

# Run installation of requirements
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Set working directory back to main app
WORKDIR /app/

# Copy application code into image
# (Excludes any files/dirs matched by patterns in .dockerignore)
COPY . /app/

