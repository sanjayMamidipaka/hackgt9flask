from flask import Flask, render_template, request, make_response
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['nm'])
        print(1)

    else:
        print('hello there')

    return '1'


if __name__ == '__main__':
    app.run(debug=True)