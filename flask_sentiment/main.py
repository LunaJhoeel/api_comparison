from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the sentiment-analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    if request.method == 'POST':
        text = request.json.get('text', '')
        if text:
            result = sentiment_pipeline(text)
            return jsonify(result)
        else:
            return jsonify({"error": "No text provided"})

if __name__ == '__main__':
    app.run(debug=True)
