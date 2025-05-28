# save_dummy_model.py
import pickle
import os
from dummy_objects import DummyModel, DummyVectorizer

os.makedirs("D:/models", exist_ok=True)

with open("D:/models/model.pkl", "wb") as f:
    pickle.dump(DummyModel(), f)

# IMPORTANT: Save with the expected name "tfidf.pkl"
with open("D:/models/tfidf.pkl", "wb") as f:
    pickle.dump(DummyVectorizer(), f)
