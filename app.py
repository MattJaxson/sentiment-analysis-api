from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Sentiment Analysis API!"})

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # -1 (negative) to 1 (positive)

    result = {
        "text": text,
        "sentiment_score": sentiment,
        "sentiment_label": "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral"
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
