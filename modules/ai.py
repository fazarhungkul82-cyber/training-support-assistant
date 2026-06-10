from openai import OpenAI
import streamlit as st

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def ask_ai(context, question):

    with open(
        "prompts/system_prompt.txt",
        "r",
        encoding="utf-8"
    ) as f:
        system_prompt = f.read()

    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        messages=[
            {
                "role":"system",
                "content":system_prompt
            },
            {
                "role":"user",
                "content":f"""
Context:
{context}

Question:
{question}
"""
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
