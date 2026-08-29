import streamlit as st
from google import genai

st.title("AI chat")

client = genai.Client(api_key="Ab8RN6J1YIYPwItVUh1de08FEAXtuaGq_H3j3WonDdIOFiK6Hg")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Գրեք հարցը..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
