# 🚀 AI Resume Screening & Candidate Ranking System

An intelligent machine learning system that automatically screens, analyzes, and ranks resumes based on a given job description using Natural Language Processing (NLP) and similarity scoring.

---

## 📌 Project Overview

This project helps automate the hiring process by:

* Extracting text from resumes (PDF)
* Cleaning and preprocessing data
* Identifying candidate skills
* Matching resumes with job descriptions
* Ranking candidates based on suitability
* Highlighting missing skills (skill gap analysis)

---

## 🎯 Features

✔ Resume text extraction (PDF parsing)
✔ Text cleaning & preprocessing
✔ Skill extraction using keyword matching / NLP
✔ Job description matching
✔ Candidate ranking using similarity score
✔ Skill gap identification
✔ Simple UI using Streamlit

---

## 🧠 Tech Stack

* Python
* spaCy / NLTK (NLP)
* Scikit-learn (Machine Learning)
* PDFPlumber (Resume parsing)
* Streamlit (Frontend UI)

---

## 🧮 How It Works

1. Upload resumes (PDF format)
2. System extracts text from resumes
3. Text is cleaned and processed
4. Skills are extracted from resumes
5. Job description is input by user
6. TF-IDF converts text into vectors
7. Cosine similarity calculates matching score
8. Candidates are ranked based on score
9. Missing skills are identified

---

## 📊 Core Formula

Similarity between resume and job description:

Similarity(A, B) = (A · B) / (||A|| ||B||)

---

## 📁 Project Structure

```
resume_screening/
│── app.py
│── parser.py
│── skill_extractor.py
│── ranking.py
│── utils.py
│── requirements.txt
│── README.md
│── sample_resumes/
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/your-username/resume-screening.git
cd resume-screening
```

Install dependencies:

```
pip install -r requirements.txt
```

Download NLP resources:

```
python -m nltk.downloader stopwords
python -m spacy download en_core_web_sm
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

---

## 📸 Output

The system provides:

* Candidate ranking (score %)
* Extracted skills
* Missing skills
* Job-fit analysis

---

## 🔥 Example Output

Candidate: John Doe
Score: 87%

Matched Skills:
✔ Python
✔ Machine Learning

Missing Skills:
❌ SQL
❌ Deep Learning

---

## 💡 Future Improvements

* Use BERT for advanced NLP
* Resume classification (job role prediction)
* Better UI/UX design
* Integration with job portals
* Database support (MongoDB / MySQL)

---

## 💼 Use Cases

* HR automation
* Recruitment platforms
* Campus placements
* Freelancing platforms

---

## 👨‍💻 Author

**Manoj Badhan**
B.Tech AI & Robotics Engineering

---

## ⭐ Support

If you found this project helpful, please give it a ⭐ on GitHub!

---
