from flask import Flask, render_template, request, jsonify
from langchain.llms import OpenAI
import os

os.environ['OPENAI_API_KEY'] = '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'

llm = OpenAI(temperature=0.3)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate_response():
    name = request.form['name']
    response = llm.predict(name)
    return jsonify({'response': response})

@app.route('/pass', methods=['POST'])
def display_response():
    name = request.form['name']
    response = llm.predict(name)
    return render_template('pass.html', ans=response)

if __name__ == '__main__':
    app.run(debug=True)