import streamlit as st
import google.generativeai as genai

st.title("AI chat")

genai.configure(api_key="ՔՈ_API_KEY")AQ.Ab8RN6L7OXwARLBuLyl0len9qXh-3tGmnhtFMuh1hAC5ajQIhQ
model = genai.GenerativeModel("gemini-2.5-flash")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Գրեք հարցը..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
    response = model.generate_content(prompt)

    with st.chat_message("assistant"):
        st.markdown(response.text)

except Exception as e:
    st.write(type(e))
    st.write(repr(e))
    st.error(str(e))
