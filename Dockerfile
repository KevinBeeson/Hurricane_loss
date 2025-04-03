FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copy local app files into container
COPY . /app

# Install Python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


# Run Streamlit app
CMD ["python", "gethurricaneloss.py", "-n", "50000", "1", "2.3", "1", "2", "2", "1", "-ncpu", "4"]
