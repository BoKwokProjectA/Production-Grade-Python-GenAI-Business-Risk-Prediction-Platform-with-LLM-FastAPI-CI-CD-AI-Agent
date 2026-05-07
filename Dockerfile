# Dockerfile optimized for RunPod (GPU support)

FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip \
    git \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy project code
COPY src/ ./src/
COPY .env.example .env

EXPOSE 8000

# Run command for RunPod
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
