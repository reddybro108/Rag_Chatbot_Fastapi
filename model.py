import os
import pickle

# Build full paths
base_dir = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(base_dir, "models", "model.pkl")
vectorizer_path = os.path.join(base_dir, "models", "tfidf.pkl")

# Load model
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)
