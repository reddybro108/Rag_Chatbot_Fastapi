import os
import pickle
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_pickle(file_path: str):
    try:
        with open(file_path, "rb") as f:
            obj = pickle.load(f)
            logger.info(f"Successfully loaded: {file_path}")
            return obj
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error loading {file_path}: {e}")
        raise

# Determine base directory (app/ directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Default relative paths (can be overridden by env vars)
DEFAULT_MODEL_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "models", "model.pkl"))
DEFAULT_VECTORIZER_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "models", "tfidf.pkl"))

# Environment-variable override (for Docker or deployment flexibility)
MODEL_PATH = os.getenv("MODEL_PATH", DEFAULT_MODEL_PATH)
VECTORIZER_PATH = os.getenv("VECTORIZER_PATH", DEFAULT_VECTORIZER_PATH)

# Load the model and vectorizer
model = load_pickle(MODEL_PATH)
vectorizer = load_pickle(VECTORIZER_PATH)
