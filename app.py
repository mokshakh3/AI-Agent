import streamlit as st
from agent import execute_agent

st.set_page_config(
    page_title="AI Agent Workspace",
    page_icon="🤖",
    layout="wide"
)
# Hide Streamlit UI Elements
st.markdown("""
<style>

/* Hide Streamlit Header */
header {
    visibility: hidden;
}

/* Hide Toolbar */
[data-testid="stToolbar"] {
    display: none !important;
}

/* Hide Top Decoration */
[data-testid="stDecoration"] {
    display: none !important;
}

/* Hide Status Widget */
[data-testid="stStatusWidget"] {
    display: none !important;
}

/* Hide Main Menu */
#MainMenu {
    visibility: hidden;
}

/* Hide Footer */
footer {
    visibility: hidden;
}

/* Remove top padding */
.block-container {
    padding-top: 1rem;
}

</style>
""", unsafe_allow_html=True)


st.title("🤖 AI Agent Workspace")
st.caption("Agentic AI System using Gemini + LangChain")

st.markdown("---")

tool = st.selectbox(
    "Select AI Tool",
    [
        "🌐 Web Search",
        "📄 PDF Summarizer",
        "📝 Text Summarizer",
        "🧠 AI Reasoning"
    ]
)

st.markdown("---")

uploaded_pdf = None
user_input = ""

# ---------------- TOOL UI ---------------- #

if tool == "🌐 Web Search":

    st.subheader("🌐 Web Search")

    user_input = st.text_input(
        "Enter your search query",
        placeholder="Example: What is Artificial Intelligence?"
    )

elif tool == "📄 PDF Summarizer":

    st.subheader("📄 PDF Summarizer")

    uploaded_pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

elif tool == "📝 Text Summarizer":

    st.subheader("📝 Text Summarizer")

    user_input = st.text_area(
        "Paste your text",
        height=220,
        placeholder="Paste any paragraph here..."
    )

elif tool == "🧠 AI Reasoning":

    st.subheader("🧠 AI Reasoning")

    user_input = st.text_area(
        "Ask your question",
        height=220,
        placeholder="Example: Compare Python and Java for AI."
    )

st.markdown("---")

execute = st.button(
    "🚀 Execute",
    use_container_width=True
)

result_box = st.empty()

if execute:

    with st.spinner("AI Agent is processing..."):

        result = execute_agent(
            tool,
            user_input,
            uploaded_pdf
        )

    result_box.success(result)

    st.download_button(
        label="📥 Download Result",
        data=result,
        file_name="AI_Result.txt",
        mime="text/plain",
        use_container_width=True
    )