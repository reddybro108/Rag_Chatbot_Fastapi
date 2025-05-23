from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_intent():
    response = client.post("/predict/", json={"user_input": "Book a flight"})
    assert response.status_code == 200
    assert "intent" in response.json()