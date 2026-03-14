import os

LLM_MODEL = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-small"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
TOP_K = 4

DATA_PATH = "data/sample_docs"

# OpenAI API key from environment variable
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', 'your_api_key_here')