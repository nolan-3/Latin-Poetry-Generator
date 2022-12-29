from flask import Flask, render_template, request, redirect, url_for
from generator import generate
import higherLower
import random
from higherLower import check

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
        #get a starting pair
        options = check.randomPair()
        option1 = options[0]
        option1 = options[1]
        # only display the word 
        return render_template("higherLower.html", option1 = option1[0], option2 = option2[0])

    if request.method == "POST":
        value = request.form["submit_button"]
        print("guess is" + value)
        print("option1 is " + option1)
        print("option2 is " + option2)
        testing = check.check(value, option1, option2)
        option1 = testing[0]
        option2 = testing[1]
        #print(testing[0], option1, option2)
        if(testing[0] == True):
            print("correct")
        elif(testing[0] == False):
            print("game over")
        options = check.randomPair()
        print(options)
        return render_template("higherLower.html")


if __name__ == '__main__':
        app.run(debug=True, port = 8000)
