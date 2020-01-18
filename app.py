from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is the index page</h1>'