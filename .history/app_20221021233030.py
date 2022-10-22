from flask import Flask, render_template, request, make_response
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
	user = request.form["nm"]
	return redirect(url_for("user", usr=user))
    else:
	return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)