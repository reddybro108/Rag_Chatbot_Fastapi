# Rag_Chatbot_Fastapi

A FastAPI-based chatbot that predicts user intents using a machine learning model, with text preprocessing powered by NLTK. The project is containerized with Docker and includes a GitHub Actions CI/CD pipeline for automated testing and deployment to Docker Hub.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Docker Setup](#docker-setup)
- [CI/CD Pipeline](#cicd-pipeline)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview
`Rag_Chatbot_Fastapi` is a Python-based chatbot built with FastAPI, designed to process user inputs and predict intents using a scikit-learn model. It leverages NLTK for text preprocessing and is deployed as a Docker container. The project includes automated testing with pytest and a GitHub Actions workflow for continuous integration and deployment to Docker Hub (`reddybro108/fastapi-docker-app`).

The chatbot supports intents like booking flights, canceling bookings, and generating wedding invitations, making it suitable for various conversational use cases.

## Features
- **FastAPI Backend**: High-performance API for intent prediction.
- **Machine Learning**: Uses scikit-learn’s `DummyClassifier` for intent classification (extendable to other models).
- **Text Preprocessing**: NLTK for tokenization and stopword removal.
- **Dockerized**: Containerized for easy deployment.
- **CI/CD**: Automated testing and deployment via GitHub Actions.
- **Testing**: Unit tests with pytest for API endpoints.
- **Support for Wedding Queries**: Handles wedding-related intents (e.g., generating invitations).

## Prerequisites
- **Python**: 3.13
- **Docker**: Desktop or CLI for containerization
- **Git**: For cloning the repository
- **Postman**: For testing API endpoints (optional)
- **GitHub Account**: For accessing CI/CD secrets
- **Docker Hub Account**: For pushing/pulling images

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/reddybro108/Rag_Chatbot_Fastapi.git
   cd Rag_Chatbot_Fastapi
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv ragenv
   .\ragenv\Scripts\Activate.ps1  # Windows
   source ragenv/bin/activate  # Linux/macOS
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK Data**:
   ```bash
   python -c "import nltk; nltk.download('punkt', download_dir='nltk_data'); nltk.download('stopwords', download_dir='nltk_data')"
   ```

5. **Generate Model Files** (if not present):
   ```bash
   python model.py
   ```
   This creates `model.pkl` and `vectorizer.pkl` for intent prediction.

## Usage
1. **Run the FastAPI Application**:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

2. **Test with Postman**:
   - **Method**: `POST`
   - **URL**: `http://127.0.0.1:8000/predict/`
   - **Headers**: `Content-Type: application/json`
   - **Body** (raw, JSON):
     ```json
     {
       "user_input": "Book a flight"
     }
     ```
   - **Expected Response**:
     ```json
     {
       "intent": "book_flight"
     }
     ```

3. **Wedding Queries**:
   Try wedding-related inputs:
   ```json
   {
     "user_input": "Generate a wedding invitation"
   }
   ```

## API Endpoints
- **POST `/predict/`**
  - **Description**: Predicts the intent of a user’s input.
  - **Request Body**:
    ```json
    {
      "user_input": "string"
    }
    ```
  - **Response**:
    ```json
    {
      "intent": "predicted_intent"
    }
    ```

## Testing
1. **Run Tests**:
   ```bash
   python -m pytest tests
   ```
   Tests in `tests/test_api.py` verify the `/predict/` endpoint for various inputs, including wedding queries.

2. **Add New Tests**:
   Modify `tests/test_api.py` to add test cases for additional intents.

## Docker Setup
1. **Build the Docker Image**:
   ```bash
   docker build -t reddybro108/fastapi-docker-app:latest .
   ```

2. **Run the Container**:
   ```bash
   docker run -d -p 8000:8000 --name fastapi-docker-app reddybro108/fastapi-docker-app:latest
   ```

3. **Test the API**:
   Use Postman to send requests to `http://127.0.0.1:8000/predict/`.

4. **Push to Docker Hub** (requires login):
   ```bash
   docker login -u reddybro108
   docker push reddybro108/fastapi-docker-app:latest
   ```

## CI/CD Pipeline
The project uses GitHub Actions for automated testing and deployment, defined in `.github/workflows/main.yml`.

- **Workflow Steps**:
  - **Build Job**:
    - Checks out code.
    - Sets up Python 3.13.
    - Installs dependencies from `requirements.txt`.
    - Runs syntax checks (`python -m py_compile main.py`).
    - Executes tests (`pytest tests/`).
  - **Dockerize Job**:
    - Logs in to Docker Hub using secrets (`DOCKER_USERNAME`, `DOCKER_PASSWORD`).
    - Builds and pushes the Docker image to `reddybro108/fastapi-docker-app:latest`.

- **Setup Secrets**:
  - Go to `Settings > Secrets and variables > Actions > Repository secrets` in your GitHub repository.
  - Add:
    - `DOCKER_USERNAME`: Your Docker Hub username.
    - `DOCKER_PASSWORD`: Your Docker Hub personal access token.

- **Monitor Workflow**:
  Check runs at `https://github.com/reddybro108/Rag_Chatbot_Fastapi/actions`.

## Project Structure
```
Rag_Chatbot_Fastapi/
├── .github/
│   └── workflows/
│       └── main.yml        # GitHub Actions CI/CD pipeline
├── tests/
│   └── test_api.py         # Pytest unit tests
├── nltk_data/              # NLTK data (punkt, stopwords)
├── .dockerignore           # Docker ignore rules
├── Dockerfile              # Docker configuration
├── main.py                 # FastAPI application
├── model.py                # Model training and loading
├── preprocess.py           # Text preprocessing with NLTK
├── requirements.txt        # Python dependencies
├── model.pkl               # Trained model
├── vectorizer.pkl          # TF-IDF vectorizer
└── README.md               # Project documentation
```

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please follow the code style and include tests for new features.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.