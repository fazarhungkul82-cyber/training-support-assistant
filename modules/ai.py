import streamlit as st
from google import genai

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

def ask_ai(context, question):

    prompt = f"""
    Anda adalah Training Support Assistant.

    Konteks SOP:
    {context}

    Pertanyaan:
    {question}

    Jawab hanya berdasarkan konteks SOP.
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text
