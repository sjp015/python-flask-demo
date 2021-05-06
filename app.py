from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, You're using Python App"

app.run(debug=True, host='0.0.0.0')
