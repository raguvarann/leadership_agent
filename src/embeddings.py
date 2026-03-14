from openai import OpenAI

client = OpenAI()

def get_embeddings(texts, model):
    response = client.embeddings.create(
        model=model,
        input=texts
    )
    return [item.embedding for item in response.data]