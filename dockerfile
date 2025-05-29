# Use Python 3.13 slim base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    python -c "import nltk; nltk.download('punkt', download_dir='/app/nltk_data'); nltk.download('stopwords', download_dir='/app/nltk_data')"

# Set NLTK data path
ENV NLTK_DATA=/app/nltk_data

# Copy project files
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to run FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# # Use Python 3.13 slim base image
# FROM python:3.13-slim

# # Set working directory
# WORKDIR /app

# # Copy requirements file and install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy NLTK data
# COPY nltk_data /app/nltk_data
# ENV NLTK_DATA=/app/nltk_data

# # Copy project files
# COPY . .

# # Expose port 8000 for FastAPI
# EXPOSE 8000

# # Command to run FastAPI app
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



