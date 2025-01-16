# Use a base image with Python installed
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY gcp_auth/ gcp_auth/
ENV GOOGLE_APPLICATION_CREDENTIALS=gcp_auth/dtumlops-447720-a5add0f7744a.json

# Install DVC with GCS support
RUN pip install --no-cache-dir \
    dvc[gs] \
    google-auth \
    google-auth-oauthlib \
    google-cloud-storage

RUN dvc init --no-scm
COPY .dvc/config .dvc/config
COPY *.dvc .dvc/
RUN dvc config core.no_scm true
RUN dvc pull

# Set a default command for the container
CMD ["bash"]
