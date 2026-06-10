import streamlit as st
import google.generativeai as genai

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-3-flash-preview"
)

def ask_ai(context, question):

    prompt = f"""
Anda adalah Training Support Assistant.

Konteks SOP:
{context}

Pertanyaan:
{question}

Jawab hanya berdasarkan SOP.
Jika tidak ada informasi, katakan tidak ditemukan.
"""

    response = model.generate_content(
        prompt
    )

    return response.text
