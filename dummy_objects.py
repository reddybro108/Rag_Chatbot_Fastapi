# dummy_objects.py
class DummyModel:
    def predict(self, X):
        return ["This is a dummy prediction"] * len(X)

class DummyVectorizer:
    def transform(self, X):
        return X
