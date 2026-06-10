import streamlit as st

from modules.rag import read_pdf
from modules.ai import ask_ai

st.set_page_config(
    page_title="Training Support Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Training Support Assistant")

uploaded_file = st.file_uploader(
    "Upload SOP PDF",
    type=["pdf"]
)

if uploaded_file:

    context = read_pdf(uploaded_file)

    st.success("SOP berhasil dibaca")

    question = st.text_input(
        "Tanyakan sesuatu tentang SOP"
    )

    if st.button("Tanya AI"):

        with st.spinner("Menganalisis SOP..."):

            answer = ask_ai(
                context,
                question
            )

        st.markdown(answer)
