from fastapi import APIRouter
from pydantic import BaseModel
from app.model import model, vectorizer

router = APIRouter()

class QueryRequest(BaseModel):
    text: str

@router.post("/predict")
async def predict_intent(query: QueryRequest):
    vec = vectorizer.transform([query.text])
    prediction = model.predict(vec)[0]
    return {"intent": prediction}
