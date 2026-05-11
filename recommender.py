import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("index.faiss")

with open("catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

def search_assessments(query, top_k=5):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding),
        top_k
    )

    results = []
    seen = set()

    for idx in indices[0]:

        if idx >= len(catalog):
            continue

        item = catalog[idx]

        name = item.get("name", "Unknown Assessment")

        if name not in seen:

            results.append(item)

            seen.add(name)

    return results