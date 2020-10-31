from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("Frontend.html")

@app.route('/start')
def start():
    return render_template("index.html")

@app.route('/instructions')
def instructions():
    return render_template("instructions.html")

@app.route("/submit")
def submit():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)