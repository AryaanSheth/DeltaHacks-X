from flask import Flask
import json

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/hello/<name>/', methods=['GET', 'POST'])
def hello(name):
    return "Hello " + name + "!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
