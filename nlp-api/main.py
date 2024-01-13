from flask import Flask
import json
from nlp import cosine_sim

app = Flask(__name__)

@app.route('/ping/', methods=['GET', 'POST'])
def welcome():
    return "pong"

@app.route('/sim/<ticket>/<pdf>', methods=['GET', 'POST'])
def sim(ticket, pdf):
    return json.dumps(cosine_sim(path, ticket))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
