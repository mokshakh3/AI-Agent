from config import model

def summarize_text(text):

    if not text.strip():
        return "Please enter some text."

    prompt = f"""
Summarize the following text in simple bullet points.

Text:
{text}
"""

    response = model.generate_content(prompt)

    return response.text