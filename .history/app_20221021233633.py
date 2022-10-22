from flask import Flask, render_template, request, make_response
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/postrequest', methods=['POST', 'GET'])
def postrequest():
    return


if __name__ == '__main__':
    app.run(debug=True)