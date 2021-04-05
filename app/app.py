import pickle

from flask import Flask, render_template, request

phone_numbers = []
with open("data.pickle", "rb") as file:
    phone_numbers = pickle.load(file)

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        phone_nubmer = request.form["phone"]
        found = False
        if phone_nubmer in phone_numbers:
            found = True
            return render_template("application/results.html", found=found)
        return render_template("application/results.html", found=found)
    return render_template("application/index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
