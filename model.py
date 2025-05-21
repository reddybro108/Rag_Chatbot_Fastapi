import pickle

with open("app/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("app/tfidf.pkl", "rb") as f:
    vectorizer = pickle.load(f)
