import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    return text.lower().strip()
