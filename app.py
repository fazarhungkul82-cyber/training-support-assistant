import streamlit as st

from modules.ai import ask_ai
from modules.rag import retrieve_relevant_pdf

# ======================
# PAGE CONFIG
# ======================

st.set_page_config(
    page_title="Training Support Assistant",
    page_icon="🎓",
    layout="wide"
)

# ======================
# SIDEBAR
# ======================

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

# ======================
# SOP ASSISTANT
# ======================

if mode == "📚 SOP Assistant":

    st.title("📚 SOP Assistant")

    question = st.text_input(
        "Tanyakan sesuatu terkait SOP"
    )

    if st.button("🔍 Cari Jawaban"):

        if question:

            try:

                doc = retrieve_relevant_pdf(
                    question
                )

                st.info(
                    f"SOP yang digunakan: {doc['filename']}"
                )

                answer = ask_ai(
                    doc["content"],
                    question
                )

                st.markdown("### Jawaban")
                st.write(answer)

            except Exception as e:

                st.error(
                    f"Terjadi kesalahan: {e}"
                )

        else:

            st.warning(
                "Silakan masukkan pertanyaan."
            )

# ======================
# WA GENERATOR
# ======================

elif mode == "📱 WA Generator":

    st.title("📱 WA Generator")

    detail = st.text_area(
        "Masukkan informasi kegiatan",
        height=200
    )

    if st.button("📨 Generate WA"):

        if detail:

            prompt = f"""
Buatkan pesan WhatsApp profesional.

Informasi kegiatan:

{detail}

Gunakan bahasa formal, ramah, dan siap kirim.
"""

            result = ask_ai(
                "",
                prompt
            )

            st.markdown("### Hasil")

            st.text_area(
                "",
                result,
                height=300
            )

        else:

            st.warning(
                "Masukkan detail kegiatan terlebih dahulu."
            )

# ======================
# EMAIL GENERATOR
# ======================

elif mode == "📧 Email Generator":

    st.title("📧 Email Generator")

    detail = st.text_area(
        "Masukkan detail email",
        height=200
    )

    if st.button("📩 Generate Email"):

        if detail:

            prompt = f"""
Buatkan email profesional.

Informasi:

{detail}

Struktur:
- Subject
- Salam Pembuka
- Isi Email
- Penutup
"""

            result = ask_ai(
                "",
                prompt
            )

            st.markdown("### Draft Email")

            st.text_area(
                "",
                result,
                height=400
            )

        else:

            st.warning(
                "Masukkan detail email terlebih dahulu."
            )

# ======================
# CHECKLIST BUILDER
# ======================

elif mode == "✅ Checklist Builder":

    st.title("✅ Checklist Builder")

    program = st.selectbox(
        "Pilih Jenis Program",
        [
            "CAPM",
            "FLDP",
            "Leadership Development",
            "Certification Program",
            "Workshop",
            "Inhouse Training"
        ]
    )

    if st.button("📝 Generate Checklist"):

        prompt = f"""
Buat checklist operasional lengkap
untuk program {program}.

Kelompokkan menjadi:

1. Pra Pelatihan
2. Saat Pelatihan
3. Pasca Pelatihan

Gunakan format checklist.
"""

        result = ask_ai(
            "",
            prompt
        )

        st.markdown("### Checklist")

        st.write(result)
