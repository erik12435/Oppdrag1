
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hjem():
    return render_template("index.html")


@app.route("/produkter")
def produkter():
    return render_template("produkter.html")


@app.route("/om")
def om():
    return render_template("om.html")


@app.route("/bestilling", methods=["GET", "POST"])
def bestilling():
    if request.method == "POST":
        navn = request.form.get("navn")
        produkt = request.form.get("produkt")
        antall = request.form.get("antall")

        return render_template(
            "bestilling.html",
            navn=navn,
            produkt=produkt,
            antall=antall
        )

    return render_template("bestilling.html")


if __name__ == "__main__":
    app.run(debug=True)
