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
if mode == "📚 SOP Assistant":

    st.header("📚 SOP Assistant")

    question = st.text_input(
        "Tanyakan SOP"
    )

    if st.button("Cari Jawaban"):

        doc = retrieve_relevant_pdf(
            question
        )

        answer = ask_ai(
            doc["content"],
            question
        )

        st.success(
            f"SOP digunakan: {doc['filename']}"
        )

        st.write(answer)
        elif mode == "📱 WA Generator":

    st.header("📱 WA Generator")

    detail = st.text_area(
        "Masukkan informasi kegiatan"
    )

    if st.button("Generate WA"):

        prompt = f"""
Buatkan pesan WhatsApp profesional.

Informasi:
{detail}

Gunakan bahasa formal dan ramah.
"""

        result = ask_ai(
            "",
            prompt
        )

        st.text_area(
            "Hasil",
            result,
            height=250
        )
        elif mode == "📧 Email Generator":

    st.header("📧 Email Generator")

    detail = st.text_area(
        "Masukkan detail email"
    )

    if st.button("Generate Email"):

        prompt = f"""
Buatkan email profesional.

Informasi:
{detail}
"""

        result = ask_ai(
            "",
            prompt
        )

        st.text_area(
            "Draft Email",
            result,
            height=350
        )
elif mode == "✅ Checklist Builder":

    st.header("✅ Checklist Builder")

    program = st.selectbox(
        "Jenis Program",
        [
            "CAPM",
            "FLDP",
            "Leadership",
            "Certification"
        ]
    )

    if st.button("Generate Checklist"):

        prompt = f"""
Buat checklist operasional lengkap
untuk program {program}.

Format:
- Pra Pelatihan
- Saat Pelatihan
- Pasca Pelatihan
"""

        result = ask_ai(
            "",
            prompt
        )

        st.write(result)
