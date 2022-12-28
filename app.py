from flask import Flask, render_template, request, redirect, url_for
from generator import generate

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html",)
    elif request.method == "POST":
        poem = request.form.get("text")
        return redirect(url_for('poemDisplay', poem=poem))


@app.route('/poem', methods = ["GET", "POST"])
def poemDisplay():
    if request.method == "GET":
        poem = request.args.get('poem', None)
        return render_template("poem.html", poem = generate(poem))
    if request.method == "POST":
        return redirect('/')

@app.route('/about', methods = ["GET", "POST"])
def about():
    if request.method == "GET":
        return render_template("about.html")
    if request.method == "POST":
        return redirect('/')

@app.route('/higherLower', methods=["GET", "POST"])
def higherLower():
    if request.method == "GET":
        return render_template("higherLower.html")


if __name__ == '__main__':
        app.run(debug=True, port = 8000)
