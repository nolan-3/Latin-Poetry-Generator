from flask import Flask, render_template, request
#from views import views

app = Flask(__name__)
#app.register_blueprint(views, url_prefix="/views")
 
if __name__ == '__main__':
        app.run(debug=True, port = 8000)
        
@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html",)
    elif request.method == "POST":
        poemDisplay()


@app.route('/poemDisplay', methods = ["GET", "POST"])
def poemDisplay():
    if request.method == "GET":
        return render_template("poem.html", poem = "test poem")
    if request.method == "POST":
        home()
