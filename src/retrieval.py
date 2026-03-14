import numpy as np

def retrieve(query_embedding, index, chunks, top_k=4):
    distances, indices = index.search(
        np.array([query_embedding]).astype("float32"),
        top_k
    )

    return [chunks[i] for i in indices[0]]