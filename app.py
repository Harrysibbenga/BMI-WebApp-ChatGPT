from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods = [ "POST" ])
def calculate():
    height = float(request.form.get("height"))
    weight = float(request.form.get("weight"))
    bmi = round(weight/((height/100) ** 2), 2)
    return render_template("result.html", bmi = bmi)


if __name__=="__main__":
    app.run(debug = True)
