from flask import Flask, render_template, request, redirect, url_for
from generator import generate
import random

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
        data = generate(poem)
        poem = data[0]
        translation = data[1]
        return render_template("poem.html", poem = poem, translation = translation)
    if request.method == "POST":
        return redirect('/')

@app.route('/about', methods = ["GET", "POST"])
def about():
    if request.method == "GET":
        return render_template("about.html")
    if request.method == "POST":
        return redirect('/')


if __name__ == '__main__':
        app.run(debug=True, port = 8000)
