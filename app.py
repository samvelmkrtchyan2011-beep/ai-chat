import streamlit as st
import google.generativeai as genai

st.title("AI chat")

genai.configure(api_key="Ab8RN6J1YIYPwItVUh1de08FEAXtuaGq_H3j3WonDdIOFiK6Hg")
model = genai.GenerativeModel("gemini-1.5-pro")

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
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
