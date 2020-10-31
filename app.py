from flask import Flask, render_template
import detector
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


@app.route("/check")
def check():
    for data in detector.check_plagiarism():
        print(data)
    return str(data)

if __name__ == "__main__":
    app.run(debug=True)