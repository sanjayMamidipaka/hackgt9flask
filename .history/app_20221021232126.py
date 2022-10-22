from flask import Flask, render_template, request, make_response
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/method', methods=['POST'])
def index():
    print(request)


if __name__ == '__main__':
    app.run(debug=True)