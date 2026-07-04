from config import model


def web_search(query):

    prompt = f"""
You are an AI assistant.

Answer the following question using your knowledge.

Question:
{query}

Give a clear and detailed answer.
"""

    response = model.generate_content(prompt)

    return response.text