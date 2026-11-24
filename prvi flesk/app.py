from flask import Flask, render_template, request
import random as r

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/o-meni")
def about_me():
    return render_template("about.html")

# met kocke med 1 - 6
@app.route("/kocka")
def dice():
    return render_template("dice.html", kocka = r.randint(1, 6))

@app.route("/kocka/<n>")
def dice2(n):
    return render_template("dice.html", kocka = r.randint(1, int(n)))

sez = [1, 2, 4]


# vaja

@app.route("/test_ljubezni", methods=["GET", "POST"])
def test_of_love():

    mosko = ""
    zensko = ""
    ljubezen = None

    if request.method == "POST":
        mosko = request.form["mosko"]
        zensko = request.form["zensko"]
        ljubezen = r.randint(0, 100)

    return render_template(
        "test_of_love.html",
        mosko=mosko,
        zensko=zensko,
        ljubezen=ljubezen
    )

app.run(debug = True)