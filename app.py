import os
import idea_generator
from flask import Flask, render_template, request, redirect, session
import simplejson


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    """Respond to incoming requests."""
    return render_template('index.html')

@app.route('/tellme', methods=['POST', 'GET'])
def generate():
    return simplejson.dumps({"idea": idea_generator.generate_idea()})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug="true")
