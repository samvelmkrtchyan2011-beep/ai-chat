import streamlit as st
import google.generativeai as genai

genai.configure(api_key="(AQ.Ab8RN6Iw7sYeZdpp3PGyfZ8rVp1R-eRzTIjZ3afKivnpt4cimg")

st.title("AI chat")let model = GenerativeModel(name: "gemini-1.5-flash-latest", apiKey: "AIzaSyAb8RN6J770hc4qBibq-7gxU994xIdObH4UwxnxqbjXWPlFE9jQ")

    var body: some View {
        VStack {

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
