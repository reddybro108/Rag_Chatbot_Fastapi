import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Load dataset
df = pd.read_csv("cleaned_chatbot_dataset.csv")
X = df["User Input"]
y = df["Intent"]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)

# Model
model = LogisticRegression()
model.fit(X_tfidf, y)

# Create models folder if not exists
os.makedirs("models", exist_ok=True)

# Save model and vectorizer
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/tfidf.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved to 'models/'")
