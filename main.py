import os
import numpy as np

from config import *
from src.document_loader import load_documents
from src.chunking import chunk_text
from src.embeddings import get_embeddings
from src.vector_store import build_index
from src.retrieval import retrieve
from src.llm import generate_answer
from src.visualization import plot_chunk_distribution


def main():

    print("Loading documents...")
    docs = load_documents(DATA_PATH)

    print("Chunking documents...")
    all_chunks = []

    for doc in docs:
        all_chunks.extend(chunk_text(doc, CHUNK_SIZE, CHUNK_OVERLAP))

    plot_chunk_distribution(all_chunks)    

    print("Creating embeddings...")
    chunk_embeddings = get_embeddings(all_chunks, EMBEDDING_MODEL)

    print("Building vector index...")
    index = build_index(chunk_embeddings)

    questions = [
        "What is our current revenue trend?",
        "Which risks were highlighted?",
        "What are the key strategic priorities?"
    ]

    for question in questions:

        print("\nQUESTION:", question)

        print("Embedding question...")
        question_embedding = get_embeddings([question], EMBEDDING_MODEL)[0]

        print("Retrieving relevant context...")
        relevant_chunks = retrieve(
            question_embedding,
            index,
            all_chunks,
            TOP_K
        )

        context = "\n\n".join(relevant_chunks)

        print("Generating answer...\n")

        answer = generate_answer(
            LLM_MODEL,
            context,
            question
        )

        print(answer)
        print("-" * 80)


if __name__ == "__main__":
    main()