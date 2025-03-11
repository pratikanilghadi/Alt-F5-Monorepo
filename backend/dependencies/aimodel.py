from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-tranformers/all-MiniLM-L6-v2")

def fetch_model():
    return model