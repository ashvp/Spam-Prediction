from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = joblib.load('phishing_predictor.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    
    text_vectorized = vectorizer.transform([text])
    
    prediction = model.predict(text_vectorized)
    
    result = 'Phishing' if prediction[0] == 1 else 'Not Phishing'
    
    return jsonify({'prediction': result})

def main():
    app.run(host='0.0.0.0', port=10000)