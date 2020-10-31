from flask import Flask, render_template, request
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

@app.route("/submit", methods=['POST'])
def submit():
    if(request.method == "POST"):
    
        answers = request.form
        print(answers)
        ans1 = answers["ans1"]
        ans2 = answers["ans2"]
        print(ans1, ans2)
        return render_template("success.html")
    else:
        return "Invalid Method"


@app.route("/check")
def check():
    for data in detector.check_plagiarism():
        print(data)
    return str(data)

if __name__ == "__main__":
    app.run(debug=True)