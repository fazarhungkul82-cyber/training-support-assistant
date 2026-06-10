import streamlit as st

from modules.rag import load_all_sop
from modules.ai import ask_ai

st.set_page_config(
    page_title="Training Support Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Training Support Assistant")

# Load SOP otomatis dari folder
with st.spinner("Memuat SOP..."):
    context = load_all_sop()

st.success("SOP berhasil dimuat")

st.markdown("### Tanya SOP")

question = st.text_input("Masukkan pertanyaan")

if st.button("Tanya AI"):

    if not question:
        st.warning("Tulis pertanyaan dulu")
    else:
        with st.spinner("AI sedang berpikir..."):
            answer = ask_ai(context, question)

        st.markdown("### Jawaban")
        st.write(answer)
