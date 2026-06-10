import streamlit as st

from modules.rag import read_pdf
from modules.ai import ask_ai

st.set_page_config(
    page_title="Training Support Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Training Support Assistant")
st.caption("AI Assistant untuk SOP dan Operasional Training")

# Session state
if "context" not in st.session_state:
    st.session_state.context = ""

# Upload SOP
uploaded_file = st.file_uploader(
    "Upload SOP PDF",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Membaca SOP..."):
        context = read_pdf(uploaded_file)
        st.session_state.context = context

    st.success("✅ SOP berhasil diunggah dan dibaca")

    with st.expander("Preview SOP"):
        st.text(context[:2000])

# Area pertanyaan
question = st.text_input(
    "Tanyakan sesuatu tentang SOP"
)

col1, col2 = st.columns(2)

with col1:
    ask_button = st.button("🔍 Tanya SOP")

with col2:
    clear_button = st.button("🗑️ Reset")

if clear_button:
    st.session_state.context = ""
    st.rerun()

if ask_button:

    if not st.session_state.context:
        st.warning("Upload SOP terlebih dahulu.")
    elif not question:
        st.warning("Masukkan pertanyaan.")
    else:

        with st.spinner("Gemini sedang menganalisis SOP..."):

            answer = ask_ai(
                st.session_state.context,
                question
            )

        st.markdown("### Jawaban")
        st.write(answer)
