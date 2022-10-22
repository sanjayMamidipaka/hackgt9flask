from flask import Flask, render_template, request, make_response
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/postrequest/', methods=['POST', 'GET'])
def postrequest():
    request_dict = request.json
    return request_dict['name']


if __name__ == '__main__':
    app.run(debug=True)