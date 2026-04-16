import streamlit as st
from services.exam_generator import generate_exam
from services.writing_corrector import correct_writing



st.title("Exam Generator")
level = st.selectbox("Select the exam level:", ["Beginner", "Intermediate", "Advanced"])
dyslexia = st.checkbox("Make the exam dyslexia-friendly")

if st.button("Generate Exam"):
    with st.spinner("Generating exam..."):
        exam = generate_exam(level, dyslexia)
    st.subheader("Generated Exam:")
    st.text(exam)

st.header("Writing Correction")

text = st.text_area("Paste student writing here", height=200)
if st.button("Correct writing"):
    result = correct_writing(text, level, dyslexia)


st.subheader("Results")

st.write("Grammar:", result["grammar"])
st.write("Vocabulary:", result["vocabulary"])
st.write("Structure:", result["structure"])

st.subheader("Feedback")
st.text_area("Feedback", result["feedback"], height=150)

st.header("Writing Correction")

text = st.text_area("Paste student writing here", height=200)

if st.button("Correct writing"):
    result = correct_writing(text, level, dyslexia)

    st.subheader("Results")

    st.write("Grammar:", result["grammar"])
    st.write("Vocabulary:", result["vocabulary"])
    st.write("Structure:", result["structure"])

    st.subheader("Feedback")
    st.text_area("Feedback", result["feedback"], height=150)
    st.metric("Grammar", result["grammar"])
    st.metric("Vocabulary", result["vocabulary"])
    st.metric("Structure", result["structure"])