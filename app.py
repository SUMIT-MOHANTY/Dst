from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    response = process_message(user_message)
    return jsonify({'reply': response})

def process_message(msg):
    return f'AI: You said "{msg}"'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
