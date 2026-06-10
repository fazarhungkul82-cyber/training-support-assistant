import streamlit as st
import google.generativeai as genai

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel("gemini-3-flash-preview")

def ask_ai(context, question):

    prompt = f"""
Anda adalah Training Support Assistant.

Gunakan SOP berikut sebagai sumber utama:

{context}

Pertanyaan:
{question}

Instruksi:
- Jawab hanya berdasarkan SOP
- Jika tidak ada informasi, katakan tidak tersedia
- Gunakan langkah-langkah jika berupa proses
"""

    response = model.generate_content(prompt)

    return response.text
