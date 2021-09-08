from flask import Flask

app = Flask(__name__)


@app.route('/<text>')
def say(text):
    return text


app.run(host='0.0.0.0', port=81)
