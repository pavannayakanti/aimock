from flask import Flask, request, jsonify

app = Flask(__name__)

# Extended question bank
questions = [
    {"id": 1, "question": "Explain the difference between a List and a Set in Java?", "tags": ["Java", "Collections"]},
    {"id": 2, "question": "Write code to convert a List to an array in Java.", "tags": ["Java", "Coding"]},
    {"id": 3, "question": "What is the purpose of Kubernetes namespaces?", "tags": ["Kubernetes", "DevOps"]},
    {"id": 4, "question": "Explain the difference between a Pod and a Deployment in Kubernetes.", "tags": ["Kubernetes"]},
    {"id": 5, "question": "What are the key components of a CI/CD pipeline?", "tags": ["DevOps", "CI/CD"]},
    {"id": 6, "question": "What is the purpose of a reverse proxy in API development?", "tags": ["API Development"]},
    {"id": 7, "question": "Explain the differences between REST and GraphQL APIs.", "tags": ["API Development"]},
]

@app.route('/')
def home():
    return 'Welcome to the AI Mock Interview System!'

@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.json
    answer = data.get('answer', '')
    return jsonify({"message": "Answer received", "answer": answer})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
