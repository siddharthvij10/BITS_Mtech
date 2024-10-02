FROM python:3.10-slim-buster

# Set the working directory in the container 
WORKDIR /workspace  
COPY train.py /workspace/
COPY requirements.txt /workspace/

COPY . /workspace/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Clean up unused package manager files
RUN rm -rf /var/cache/apk/*
# Set environment variables to ensure reproducibility
ENV PYTHONUNBUFFERED=1

# Default command to run the training script
CMD ["python", "train.py"]
