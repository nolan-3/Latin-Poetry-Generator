from flask import Flask, render_template, request, redirect, url_for
from generator import generate
#from views import views

app = Flask(__name__)
#app.register_blueprint(views, url_prefix="/views")


@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html",)
    elif request.method == "POST":
        #poem = generate()
        poem = request.form.get("text")
        return redirect(url_for('poemDisplay', poem=poem))
        #return redirect('/poemDisplay')


@app.route('/poemDisplay', methods = ["GET", "POST"])
def poemDisplay():
    if request.method == "GET":
        poem = request.args.get('poem', None)
        return render_template("poem.html", poem = generate(poem))
    if request.method == "POST":
        return redirect('/')
if __name__ == '__main__':
        app.run(debug=True, port = 8000)