from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return  "Hello There"

@app.route('/next')
def next():
    return  "Second Page"