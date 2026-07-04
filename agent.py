from search_tool import web_search
from tools import summarize_text
from reasoning import ai_reasoning
from pdf_tool import summarize_pdf


def execute_agent(tool, user_input, pdf_file=None):

    # Web Search
    if tool == "🌐 Web Search":

        if not user_input.strip():
            return "Please enter a search query."

        return web_search(user_input)

    # PDF Summarizer
    elif tool == "📄 PDF Summarizer":

        if pdf_file is None:
            return "Please upload a PDF."

        return summarize_pdf(pdf_file)

    # Text Summarizer
    elif tool == "📝 Text Summarizer":

        if not user_input.strip():
            return "Please enter some text."

        return summarize_text(user_input)

    # AI Reasoning
    elif tool == "🧠 AI Reasoning":

        if not user_input.strip():
            return "Please enter your question."

        return ai_reasoning(user_input)

    return "Invalid Tool Selected."