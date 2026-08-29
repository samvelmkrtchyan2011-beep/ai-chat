import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6KH_cFtOpUbfUJKUo-oamOT5C_D2Q-Y180jRGuVfUot-")

st.title("AI chat")

model = genai.GenerativeModel("gemini-1.5-flash")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Գրեք հարցը..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = model.generate_content(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
