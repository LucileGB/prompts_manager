from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/prompts")
def prompts():
    return render_template('prompts.html')