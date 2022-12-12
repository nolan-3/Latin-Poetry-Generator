# from flask import Blueprint, render_template, request

# views = Blueprint(__name__, "views")

# @views.route(__name__, methods = ["GET", "POST"])
# def home():
#     if request.method == "GET":
#         return render_template("index.html",)
#     elif request.method == "POST":
#         poemDisplay()

# @views.route('/poemDisplay', methods = ["GET", "POST"])
# def poemDisplay():
#     if request.method == "GET":
#         return render_template("poem.html", poem = "test poem")
#     if request.method == "POST":
#         home()