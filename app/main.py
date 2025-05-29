
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from preprocess import clean_text
from fastapi import FastAPI

from app.routes import router  # instead of from routes import router
from app.model import model, vectorizer


app = FastAPI()
app.include_router(router)


class Query(BaseModel):
    user_input: str

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}    

@app.post("/predict/")
async def predict_intent(query: Query):
    try:
        cleaned = clean_text(query.user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        return {"intent": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
class Query(BaseModel):
    user_input: str

@app.post("/predict1/")
def predict_intent(query: Query):
    cleaned = clean_text(query.user_input)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    return {"intent": prediction}

