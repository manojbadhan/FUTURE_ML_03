from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_texts, job_desc):
    documents = resume_texts + [job_desc]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    job_vector = tfidf_matrix[-1]

    scores = []
    for i in range(len(resume_texts)):
        score = cosine_similarity(tfidf_matrix[i], job_vector)
        scores.append(score[0][0])

    return scores