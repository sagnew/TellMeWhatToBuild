import os
from flask import Flask, render_template, request, redirect, session
from constants import CONSUMER_KEY, CONSUMER_SECRET, APP_SECRET_KEY


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    """Respond to incoming requests."""
    return render_template('index.html')

@app.route('/tellme', methods=['POST', 'GET']
def generate():
    return render_template('generated.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug="true")