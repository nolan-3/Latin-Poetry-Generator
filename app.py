from flask import Flask, render_template, request, redirect, url_for
from generator import generate
import higherLower
import random
from higherLower import check

class round:
    option1 = ''
    option2 = ''
    score = 0

obj = round()

global option1
global option2
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

    #make sure the POST if statement has access to the initial pair
    if request.method == "GET":
        #get a starting pair and set score = 0
        obj.option1 = check.randomOption()
        obj.option2 = check.randomOption()
        obj.score = 0
        #                                           only display the word 
        return render_template("higherLower.html", score = obj.score, option1 = obj.option1[0], option2 = obj.option2[0])

    if request.method == "POST":
        value = request.form["submit_button"]
        test = check.check(value, obj.option1, obj.option2)
        obj.option1 = check.randomOption()
        obj.option2 = check.randomOption()
        if(test == True):
            obj.option2 = obj.option1
            obj.option1 = check.randomOption()
            obj.score += 1
            return render_template("higherLower.html", score = obj.score, option1 = obj.option1[0], option2 = obj.option2[0])
        elif(test == False):
            return render_template("gameOver.html", score = obj.score)


if __name__ == '__main__':
        app.run(debug=True, port = 8000)
