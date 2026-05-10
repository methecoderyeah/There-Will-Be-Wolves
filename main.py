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

@app.route("/was-medieval-justice-fair")
def was_medieval_justice_fair():
    return render_template("was_medieval_justice_fair.html")

@app.route("/punishments")
def punishments():
    return render_template("punishments.html")

if __name__ == "__main__":
    app.run(debug=True)
