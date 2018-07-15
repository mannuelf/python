from flask import Flask

app = Flask(__name__)

@app.rout('/')
def home():
    return "Hello World"

app.run(port=5080)