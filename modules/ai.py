import streamlit as st
import google.generativeai as genai

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel("gemini-3-flash-preview")

def ask_ai(context, question):

    if context:

        prompt = f"""
Gunakan SOP berikut:

{context}

Pertanyaan:
{question}
"""

    else:

        prompt = question

    response = model.generate_content(
        prompt
    )

    return response.text
