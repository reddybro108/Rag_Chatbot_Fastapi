from fastapi import FastAPI
from pydantic import BaseModel
from app.preprocess import clean_text
from app.model import model, vectorizer
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

class Query(BaseModel):
    user_input: str

@app.post('/predict')
async def predict_intent(query: Query):
        try:
            cleaned = clean_text(query.user_input)
            print(f"Cleaned input: {cleaned}")  # Debugging line
            vectorized = vectorizer.transform([cleaned])
            print(f"Vectorized input: {vectorized}")
            prediction = model.predict(vectorized)[0]
            print(f"Prediction: {prediction}")
            return {"my intent": prediction}
        except Exception as e:
            print(f"Error during prediction: {e}")
