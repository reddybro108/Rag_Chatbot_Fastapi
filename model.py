# import pickle

# with open("app/model.pkl", "rb") as f:
#     model = pickle.load(f)

# with open("app/tfidf.pkl", "rb") as f:
#     vectorizer = pickle.load(f)

from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

model = joblib.load('path/to/your/model.pkl')
vectorizer = joblib.load('path/to/your/vectorizer.pkl')