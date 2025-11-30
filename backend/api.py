# Simple Flask API skeleton (optional)
from flask import Flask, request, jsonify
from app.summarizer import summarize_text
from app.mcq_generator import generate_mcqs

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json or {}
    text = data.get('text','')
    mode = data.get('mode','short')
    return jsonify({'notes': summarize_text(text, mode)})

@app.route('/mcqs', methods=['POST'])
def mcqs():
    data = request.json or {}
    text = data.get('text','')
    n = int(data.get('n',10))
    difficulty = data.get('difficulty','Mixed')
    return jsonify({'mcqs': generate_mcqs(text, n, difficulty)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
