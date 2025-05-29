# Use Python 3.13 slim base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy NLTK data
COPY nltk_data /app/nltk_data
ENV NLTK_DATA=/app/nltk_data

# Copy project files
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# # Base image
# FROM python:3.10-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# ENV MODEL_PATH=/app/models/model.pkl
# ENV VECTORIZER_PATH=/app/models/tfidf.pkl

# # Set working directory
# WORKDIR /app

# # Install OS dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     && apt-get clean

# # Copy requirements first for caching
# COPY requirements.txt .

# # Install Python dependencies
# RUN pip install --upgrade pip && pip install -r requirements.txt

# # Copy project files
# COPY app/ app/
# COPY models/ models/
# COPY data/ data/
# COPY tests/ tests/
# COPY . .

# # Expose port for FastAPI
# EXPOSE 8000

# # Start the app
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


# # Base image
# FROM python:3.9

# # Working directory
# WORKDIR /app

# # Copy files
# COPY . .

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Expose port
# EXPOSE 8000

# # Run FastAPI app
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
