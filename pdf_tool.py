from pypdf import PdfReader
from config import model


def summarize_pdf(uploaded_file):

    try:

        reader = PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        if text.strip() == "":
            return "No readable text found."

        prompt = f"""
Summarize this PDF in simple bullet points.

{text}
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"Error: {e}"