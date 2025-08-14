# Dockerfile for sim-dice-roll CLI

FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies and the package
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install -e .

# Default entry point to run the CLI
ENTRYPOINT ["sim-dice-roll"]
