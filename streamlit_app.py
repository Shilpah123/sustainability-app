import streamlit as st

st.title("AI Sustainability Agent")

uploaded_files = st.file_uploader(
    "Upload documents",
    accept_multiple_files=True
)

if uploaded_files:
    st.success("Files uploaded")
