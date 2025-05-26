
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import model, vectorizer
from preprocess import clean_text
from fastapi import FastAPI


from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router)


class Query(BaseModel):
    user_input: str

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

@app.post("/predict/")
def predict_intent(query: Query):
    cleaned = clean_text(query.user_input)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    return {"intent": prediction}

# from fastapi import FastAPI
# from pydantic import BaseModel
# from app.model import model, vectorizer
# from app.preprocess import clean_text

# app = FastAPI()

# class Query(BaseModel):
#     user_input: str

# @app.post("/predict/")
# def predict_intent(query: Query):
#     cleaned = clean_text(query.user_input)
#     vectorized = vectorizer.transform([cleaned])
#     prediction = model.predict(vectorized)[0]
#     return {"intent": prediction}