import streamlit as st

from modules.ai import ask_ai
from modules.rag import retrieve_relevant_pdf

st.set_page_config(
    page_title="Training Support Assistant",
    page_icon="🎓",
    layout="wide"
)

st.sidebar.title("🎓 Training Support Assistant")

mode = st.sidebar.radio(
    "Mode",
    [
        "📚 SOP Assistant",
        "📱 WA Generator",
        "📧 Email Generator",
        "✅ Checklist Builder"
    ]
)
