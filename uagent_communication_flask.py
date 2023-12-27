import docx2txt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)

job_description = docx2txt.process('sample_description.docx')

# Replace this with the actual method or logic to interact with your local NLP model
def get_completion(resume_text):
    # Perform the necessary steps to interact with your local NLP model
    # Replace the following with the actual logic:
    content = [job_description, resume_text]

# TF-IDF Vectorization
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(content)

# Cosine Similarity
    cosine_sim_matrix = cosine_similarity(tfidf_matrix)

# Normalization
    norm_cosine_sim_matrix = cosine_sim_matrix / np.outer(np.linalg.norm(cosine_sim_matrix, axis=1), np.linalg.norm(cosine_sim_matrix, axis=0))
    result = norm_cosine_sim_matrix[1][0]
    response_from_nlp_model = f"{result*100:.2f}"
    return response_from_nlp_model
@app.route('/get_completion', methods=['POST'])
def handle_get_completion():
    try:

        resume_text = request.get_data(as_text=True)

        # Replace the following line with the actual method or logic to interact with your local NLP model
        result = get_completion(resume_text)
        print(result)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
