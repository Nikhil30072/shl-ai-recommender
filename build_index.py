import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

texts = []

for item in catalog:

    text = f"""
    Name: {item['name']}
    Description: {item['description']}
    """

    texts.append(text)

if len(texts) == 0:
    raise Exception("No catalog data found")

embeddings = model.encode(texts)

embeddings = np.array(embeddings)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index, "index.faiss")

print("FAISS index saved successfully")