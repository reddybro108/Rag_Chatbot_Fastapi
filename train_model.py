import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv("cleaned_chatbot_dataset.csv")

# Features and labels
X = df["User Input"]
y = df["Intent"]

# TF-IDF Vectorizer
tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(X)

# Model
model = LogisticRegression()
model.fit(X_tfidf, y)

# Save model and vectorizer
with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("app/tfidf.pkl", "wb") as f:
    pickle.dump(tfidf, f)

print("Model and vectorizer saved.")
