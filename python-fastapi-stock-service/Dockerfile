FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libpq-dev \
    gcc \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files and service.proto
COPY requirements.txt setup.py service.proto ./

# Upgrade pip and install Python packages
RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir wheel setuptools \
    && python -m pip install --no-cache-dir -r requirements.txt

# Build the project (generate gRPC code)
RUN python setup.py build

# Copy the application code into /app
COPY app/ ./

# List the contents after copying app/
RUN ls -la /app

# Expose the gRPC port
EXPOSE 50051

# Command to run the application
CMD ["python", "main.py"]