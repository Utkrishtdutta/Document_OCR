import ollama
import base64
import streamlit as st


def question_query(input, uploaded_files):
    uploaded_files = base64.b64encode(uploaded_files.read()).decode('utf-8')
    response = ollama.chat(
    model="llama3.2-vision",
    messages=[{
      "role": "user",
      "content": input,
      "images": [uploaded_files]
    }],
    )
    return response.message.content


uploaded_files = st.file_uploader("Choose a Image file", type=['jpeg','png'])

if uploaded_files:
    input = st.chat_input("Enter the question")
    if input:
        output = question_query(input, uploaded_files)
        print(output)
        st.write(output)

