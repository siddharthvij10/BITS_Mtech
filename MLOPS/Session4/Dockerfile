# FROM ubuntu
FROM python:3.10-slim-buster

WORKDIR /workspace

# Copy requirements.txt
COPY requirements.txt /workspace/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . /workspace/

# Set the default command to bash
CMD ["bash"]
