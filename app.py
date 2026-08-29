import streamlit as st
import google.generativeai as genai

# Կարգավորում ենք API բանալին
genai.configureAQ.Ab8RN6KH_cFtOpUbfUJkUo-oamOT5C_D2Q-Y180jRGuVfUot-A

st.title("AI chat")

model = genai.GenerativeModel("gemini-1.5-flash")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Արտածում ենք նախորդ հաղորդագրությունները
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Եթե օգտատերը գրում է հաղորդագրություն
if prompt := st.chat_input("Գրեք հարցը..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        response = model.generate_content(prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Սխալ տեղի ունեցավ՝ {e}")
