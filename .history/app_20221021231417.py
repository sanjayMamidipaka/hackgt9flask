from flask import Flask, render_template, request, make_response
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/', )
def index():
    obj = {'ashu': 'cha', 'sanjay': 'mamidi', 'ajay':'bati'}
    return make_response(
        jsonify(obj),
        200,
    )


if __name__ == '__main__':
    app.run(debug=True)