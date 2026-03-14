# AI Leadership Insight Agent

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system that:

- Ingests company documents (annual reports, quarterly reports, strategy notes, etc.)
- Chunks documents for efficient processing
- Generates embeddings using OpenAI's text-embedding-3-small
- Stores embeddings in a FAISS vector index
- Retrieves relevant context for natural language questions
- Generates concise, factual answers using GPT-4o-mini, grounded in the documents
- Provides visualizations for data insights (e.g., chunk distributions)

The system is designed for leadership-level strategic question answering, providing natural language outputs with appropriate details and report sections.

## Requirements

- Python 3.9+
- OpenAI API Key

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

1. Obtain an OpenAI API key from [OpenAI](https://platform.openai.com/api-keys)
2. Set the API key as an environment variable:
   ```bash
   # On Windows (PowerShell)
   $env:OPENAI_API_KEY = "your_api_key_here"
   
   # On Linux/Mac
   export OPENAI_API_KEY="your_api_key_here"
   ```
   Or set it permanently in your system environment variables.

## Usage

### Running the Script

```bash
python main.py
```

This will process the documents in `data/sample_docs/`, generate visualizations, and answer the sample questions. Outputs (plots) are saved to the `outputs/` directory.

### Running the Notebook

Open `AI_Leadership_Insight_Agent.ipynb` in Jupyter and run the cells sequentially. The notebook includes:

- Code walkthrough
- Sample outputs
- Visualizations (chunk distribution plots)
- Validation notes

## Sample Questions

- "What is our current revenue trend?"
- "Which risks were highlighted?"
- "What are the key strategic priorities?"

## Assumptions

- Documents are in text (.txt) or PDF (.pdf) format
- OpenAI models used: text-embedding-3-small for embeddings, gpt-4o-mini for generation
- Chunk size: 800 characters with 100 overlap
- Top-k retrieval: 4 chunks
- Answers are grounded in retrieved context for factual accuracy

## Validation

- Tested on provided sample questions
- Outputs are natural language with details
- No specific metrics required; validation through answer quality inspection
- Can be extended with evaluation metrics for production use

## Project Structure

```
.
├── .gitignore               # Git ignore file
├── config.py                # Configuration file with model names, paths, and API key (from env)
├── main.py                  # Main script to run the agent
├── AI_Leadership_Insight_Agent.ipynb  # Jupyter notebook demonstration
├── requirements.txt         # Python dependencies
├── readme.md                # This file
├── __pycache__/             # Python bytecode cache
├── data/
│   └── sample_docs/         # Folder for company documents
├── outputs/                 # Generated visualizations and plots
└── src/
    ├── __pycache__/         # Python bytecode cache
    ├── document_loader.py   # Document ingestion
    ├── chunking.py          # Text chunking
    ├── embeddings.py        # Embedding generation
    ├── vector_store.py      # FAISS index building
    ├── retrieval.py         # Context retrieval
    ├── llm.py               # Answer generation
    └── visualization.py     # Data visualization utilities
```