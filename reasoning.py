from config import model

def ai_reasoning(question):

    prompt = f"""
You are an AI reasoning assistant.

Answer using ONLY this format:

## Analysis
(2-3 lines)

## Comparison
(Short comparison if needed)

## Recommendation
(Clear recommendation)

Question:
{question}

Keep the answer under 250 words.
"""

    response = model.generate_content(prompt)

    return response.text