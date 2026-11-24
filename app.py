from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ljubezn", methods = ["POST"])
def love_calc():
    print(request.form)
    i1= request.form["ime1"]
    i2= request.form["ime2"]
    procent=0
    if i1.strip().lower()=="patrik" or i2.strip().lower()=="patrik":
        procent = random.randint(90,100)
    else:
        procent = random.randint(0,100)

    if procent < 30:
        print("Pozabi")
    elif procent < 70:
        print("Morda")
    else:
        print("Poroka!")




    return render_template("index.html",ime1=i1,ime2= i2,p=procent) 

app.run(debug=True)