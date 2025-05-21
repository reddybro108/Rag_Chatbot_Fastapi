from fastapi import FastAPI
from pydantic import BaseModel
from app.model import model, vectorizer
from app.preprocess import clean_text

app = FastAPI()

class Query(BaseModel):
    user_input: str

@app.post("/predict/")
def predict_intent(query: Query):
    cleaned = clean_text(query.user_input)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    return {"intent": prediction}