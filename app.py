import streamlit as st
import os
from parser import extract_text_from_pdf
from utils import clean_text
from skill_extractor import extract_skills
from ranking import calculate_similarity
from ranking import cosine_similarity
from ranking import TfidfVectorizer
from skill_extractor import skills_list

st.title("AI Resume Screening System")

job_desc = st.text_area("Enter Job Description")

uploaded_files = st.file_uploader("Upload Resumes", accept_multiple_files=True)

if st.button("Analyze Candidates"):
    resume_texts = []
    names = []
    skills_data = []

    for file in uploaded_files:
        with open(file.name, "wb") as f:
            f.write(file.getbuffer())

        text = extract_text_from_pdf(file.name)
        clean = clean_text(text)

        resume_texts.append(clean)
        names.append(file.name)

        skills = extract_skills(clean)
        skills_data.append(skills)

    scores = calculate_similarity(resume_texts, job_desc)

    results = list(zip(names, scores, skills_data))
    results = sorted(results, key=lambda x: x[1], reverse=True)

    st.subheader("Ranking Results")

    for name, score, skills in results:
        st.write(f"### {name}")
        st.write(f"Score: {round(score*100,2)}%")
        st.write(f"Skills: {skills}")

        job_skills = extract_skills(clean_text(job_desc))
        missing = list(set(job_skills) - set(skills))

        st.write(f"Missing Skills: {missing}")
        st.write("---")