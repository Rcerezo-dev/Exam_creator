import streamlit as st
from services.exam_generator import generate_exam

st.title("Exam Generator")
level = st.selectbox("Select the exam level:", ["Beginner", "Intermediate", "Advanced"])
dyslexia = st.checkbox("Make the exam dyslexia-friendly")

if st.button("Generate Exam"):
    with st.spinner("Generating exam..."):
        exam = generate_exam(level, dyslexia)
    st.subheader("Generated Exam:")
    st.text(exam)