Rag_Chatbot_Fastapi
A FastAPI-based chatbot that predicts user intents using a machine learning model, with text preprocessing powered by NLTK. The project is containerized with Docker and includes a GitHub Actions CI/CD pipeline for automated testing and deployment to Docker Hub.
Table of Contents

Overview
Features
Prerequisites
Installation
Usage
API Endpoints
Testing
Docker Setup
CI/CD Pipeline
Project Structure
Contributing
License

Overview
Rag_Chatbot_Fastapi is a Python-based chatbot built with FastAPI, designed to process user inputs and predict intents using a scikit-learn model. It leverages NLTK for text preprocessing and is deployed as a Docker container. The project includes automated testing with pytest and a GitHub Actions workflow for continuous integration and deployment to Docker Hub (reddybro108/fastapi-docker-app).
The chatbot supports intents like booking flights, canceling bookings, and generating wedding invitations, making it suitable for various conversational use cases.
Features

FastAPI Backend: High-performance API for intent prediction.
Machine Learning: Uses scikit-learn’s DummyClassifier for intent classification (extendable to other models).
Text Preprocessing: NLTK for tokenization and stopword removal.
Dockerized: Containerized for easy deployment.
CI/CD: Automated testing and deployment via GitHub Actions.
Testing: Unit tests with pytest for API endpoints.
Support for Wedding Queries: Handles wedding-related intents (e.g., generating invitations).

Prerequisites

Python: 3.13
Docker: Desktop or CLI for containerization
Git: For cloning the repository
Postman: For testing API endpoints (optional)
GitHub Account: For accessing CI/CD secrets
Docker Hub Account: For pushing/pulling images

Installation

Clone the Repository:
git clone https://github.com/reddybro108/Rag_Chatbot_Fastapi.git
cd Rag_Chatbot_Fastapi


Set Up Virtual Environment:
python -m venv ragenv
.\ragenv\Scripts\Activate.ps1  # Windows
source ragenv/bin/activate  # Linux/macOS


Install Dependencies:
pip install -r requirements.txt


Download NLTK Data:
python -c "import nltk; nltk.download('punkt', download_dir='nltk_data'); nltk.download('stopwords', download_dir='nltk_data')"


Generate Model Files (if not present):
python model.py

This creates model.pkl and vectorizer.pkl for intent prediction.


Usage

Run the FastAPI Application:
uvicorn main:app --reload

The API will be available at http://127.0.0.1:8000.

Test with Postman:

Method: POST
URL: http://127.0.0.1:8000/predict/
Headers: Content-Type: application/json
Body (raw, JSON):{
  "user_input": "Book a flight"
}


Expected Response:{
  "intent": "book_flight"
}




Wedding Queries:Try wedding-related inputs:
{
  "user_input": "Generate a wedding invitation"
}



API Endpoints

POST /predict/
Description: Predicts the intent of a user’s input.
Request Body:{
  "user_input": "string"
}


Response:{
  "intent": "predicted_intent"
}





Testing

Run Tests:
python -m pytest tests

Tests in tests/test_api.py verify the /predict/ endpoint for various inputs, including wedding queries.

Add New Tests:Modify tests/test_api.py to add test cases for additional intents.


Docker Setup

Build the Docker Image:
docker build -t reddybro108/fastapi-docker-app:latest .


Run the Container:
docker run -d -p 8000:8000 --name fastapi-docker-app reddybro108/fastapi-docker-app:latest


Test the API:Use Postman to send requests to http://127.0.0.1:8000/predict/.

Push to Docker Hub (requires login):
docker login -u reddybro108
docker push reddybro108/fastapi-docker-app:latest



CI/CD Pipeline
The project uses GitHub Actions for automated testing and deployment, defined in .github/workflows/main.yml.

Workflow Steps:

Build Job:
Checks out code.
Sets up Python 3.13.
Installs dependencies from requirements.txt.
Runs syntax checks (python -m py_compile main.py).
Executes tests (pytest tests/).


Dockerize Job:
Logs in to Docker Hub using secrets (DOCKER_USERNAME, DOCKER_PASSWORD).
Builds and pushes the Docker image to reddybro108/fastapi-docker-app:latest.




Setup Secrets:

Go to Settings > Secrets and variables > Actions > Repository secrets in your GitHub repository.
Add:
DOCKER_USERNAME: Your Docker Hub username.
DOCKER_PASSWORD: Your Docker Hub personal access token.




Monitor Workflow:Check runs at https://github.com/reddybro108/Rag_Chatbot_Fastapi/actions.


Project Structure
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

Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

Please follow the code style and include tests for new features.
License
This project is licensed under the MIT License. See the LICENSE file for details.
