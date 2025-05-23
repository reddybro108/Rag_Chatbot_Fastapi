# import pickle

# with open("app/model.pkl", "rb") as f:
#     model = pickle.load(f)

# with open("app/tfidf.pkl", "rb") as f:
#     vectorizer = pickle.load(f)

from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

model = joblib.load('models/faq_model.pkl')

vectorizer = joblib.load('models/vectorizer.pkl')

import os

model_path = os.path.join(os.path.dirname(__file__), 'models', 'faq_model.pkl')
model = joblib.load(model_path)
