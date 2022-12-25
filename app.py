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


@app.route('/poemDisplay', methods = ["GET", "POST"])
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

@app.route('/christmas', methods = ["GET", "POST"])
def christmas():
    if request.method == "GET":
        return render_template("christmas.html", clue = "")
    elif request.method == "POST":
        clue = ""
        name = request.form.get("praenomen")
        name = name.strip().lower()
        if(name == 'erin'):
            clue = "A speaker in a high up place (but not the ceiling!)"
        elif(name == 'colin'):
            clue = "A fish tank?"
        elif(name == 'donna'):
            clue = "A dangerous place to retrieve ping pong balls"
        elif(name == 'sean'):
            clue = "This old communication method has recently been in high demand"
        return render_template("christmas.html", clue = clue)

if __name__ == '__main__':
        app.run(debug=True, port = 8000)