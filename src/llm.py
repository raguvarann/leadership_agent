from openai import OpenAI

client = OpenAI()

def generate_answer(model, context, question):

    prompt = f"""
You are an AI Leadership Insight Agent.

Answer ONLY using the provided context.

If information is missing, say so.

Context:
{context}

Question:
{question}

Provide a structured response:

Summary:
Key Insights:
Risks:
Recommendations:
"""

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content