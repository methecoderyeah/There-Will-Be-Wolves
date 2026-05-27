from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/what-is-justice")
def what_is_justice():
    return render_template("what_is_justice.html")

@app.route("/how-medieval-courts-worked")
def how_medieval_courts_worked():
    return render_template("how_medieval_courts_worked.html")

@app.route("/punishments-&-crimes")
def punishments():
    return render_template("punishments.html")

@app.route("/credits")
def credits_():
    return render_template("credits.html")

@app.route("/cat")
def cat():
    return render_template("cat.html")

@app.route("/sources")
def sources():
    return render_template

if __name__ == "__main__":
    app.run(debug=True)
