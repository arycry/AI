import streamlit as st
import requests

st.set_page_config(page_title="Chatbot Perikanan", page_icon="🐟")

st.title("🤖 Chatbot Perikanan")
st.markdown("Tanya apa saja seputar budidaya ikan!")

# Input user
prompt = st.text_input("Masukkan pertanyaan kamu:")

if st.button("Kirim"):
    if prompt:
        with st.spinner("Menjawab..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json={"prompt": prompt}
                )
                result = response.json()
                st.success(result["response"])
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
    else:
        st.warning("Masukkan pertanyaan dulu bro!")

