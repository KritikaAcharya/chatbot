from flask import Flask, render_template,request
import openai
from langchain.llms import OpenAI
import os

os.environ['OPENAI_API_KEY'] = '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'# OPENAI_API_KEY = ' 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'

llm = OpenAI(temperature=0.3)


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    




@app.route('/', methods=['POST'])
def getvalue():
    global name 
    name = request.form['name']

    y=llm.predict(name)
    
    return render_template('pass.html', ans=y)




if __name__=='__main__':
    app.run(debug=True)
