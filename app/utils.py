import streamlit as st
import base64

def download_button(data: str, filename: str, label: str):
    """Create a download button in Streamlit for text data."""
    b = data.encode('utf-8')
    b64 = base64.b64encode(b).decode()
    href = f"data:application/octet-stream;base64,{b64}"
    st.markdown(f"<a href=\"{href}\" download=\"{filename}\">{label}</a>", unsafe_allow_html=True)
