skills_list = [
    "python", "machine learning", "data analysis",
    "sql", "deep learning", "nlp", "tensorflow", "opencv"
]

def extract_skills(text):
    found_skills = []
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)
    return list(set(found_skills))