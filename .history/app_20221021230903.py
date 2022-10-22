from flask import Flask, render_template, request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    obj = {'ashu': 'cha, 'sanjay':}
    return 


if __name__ == '__main__':
    app.run(debug=True)