from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html.j2")

@app.route("/1")
def f1():
    return render_template("1.html.j2")

@app.route("/action", methods=["POST"])
def create():
    res = request.form
    print(res)

    return render_template("home.html.j2")

def run():
    app.run(debug=True, port=5690, host="0.0.0.0")


if __name__ == "__main__":
    run()
