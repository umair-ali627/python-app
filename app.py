from flask import Flask, jsonify, render_template, request
import datetime

app = Flask(__name__)

# Example: Home route with template rendering (if needed)
@app.route('/')
def home():
    return jsonify({
        "message": "Python! Welcome to the Advanced Flask App on /python using port 8888!",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    })

# Example: Simple API route
@app.route('/api/greet', methods=['POST'])
def greet_user():
    data = request.json
    name = data.get('name', 'Guest')
    return jsonify({
        "greeting": f"Hello, {name}!",
        "status": "success"
    })

# Example: Health check
@app.route('/health')
def health_check():
    return jsonify({
        "status": "running",
        "service": "flask-app",
        "port": 8888
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
