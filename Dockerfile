FROM python:3.12-slim

# Install system deps (IMPORTANT for your project)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy project
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Disable GPU (important for your setup)
ENV CUDA_VISIBLE_DEVICES=""

# Expose Flask port
EXPOSE 5001

# Default run (Flask)
CMD ["python", "run.py"]