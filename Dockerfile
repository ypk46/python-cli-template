FROM python:3.9-slim

# Get linux dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends gcc python3-dev build-essential -y \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /usr/src/app

# Copy requirements file
COPY . /usr/src/app/

# Install dependencies
RUN pip install -e .

# Set default starting command
ENTRYPOINT [ "pycli"]
