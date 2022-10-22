from flask import Flask, render_template, request, make_response
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    obj = {'ashu': 'cha', 'sanjay': 'mamidi', 'ajay':'bati'}
    return make_response(
        json.dumpsobj,
        200,
        headers={'Content-Type', 'application/json'}
    )


if __name__ == '__main__':
    app.run(debug=True)