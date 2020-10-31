from flask import Flask, render_template, request, url_for, redirect, session
# import detector
import yaml
from authlib.integrations.flask_client import OAuth
app = Flask(__name__)



db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)

#Oauth


# OAuth Config
app.secret_key = db['secret_key']
oauth = OAuth(app)
google = oauth.register(
    name="google",
    client_id=db['client_id'],
    client_secret=db['client_secret'],
    access_token_url="https://accounts.google.com/o/oauth2/token",
    access_token_params=None,
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    authorize_params=None,
    api_base_url="https://www.googleapis.com/oauth2/v1/",
    userinfo_endpoint=
    "https://openidconnect.googleapis.com/v1/userinfo",  # This is only needed if using openId to fetch user info
    client_kwargs={"scope": "openid email profile"},
)




@app.route('/')
def hello_world():
    email = dict(session).get("email", None)

    if(email == None):
        return redirect("/login")

    return render_template("Frontend.html")

@app.route('/start')
def start():
    email = dict(session).get("email", None)

    if(email == None):
        return redirect("/login")

    return render_template("index.html")

@app.route('/instructions')
def instructions():
    email = dict(session).get("email", None)

    if(email == None):
        return redirect("/login")

    return render_template("instructions.html")

@app.route("/submit", methods=['POST'])
def submit():
    email = dict(session).get("email", None)

    if(email == None):
        return redirect("/login")

    if(request.method == "POST"):
        
        answers = request.form
        print(answers)
        ans1 = answers["ans1"]
        ans2 = answers["ans2"]
        email = dict(session).get("email", None)

        s1 = email + "1.txt"
        f1 = open("data/question1/"+s1, "w")
        f1.write(ans1)
        f1.close()

        
        s2 = email + "2.txt"
        f2 = open("data/question2/"+s2, "w")
        f2.write(ans2)
        f2.close()
        ans2 = answers["ans2"]
        
        print(ans1, ans2)
        return redirect("/logout")
    else:
        return "Invalid Method"


@app.route("/check")
def check():
    for data in detector.check_plagiarism():
        print(data)
    return str(data)


# _______________________ AUTH ROUTES ___________________________________________

@app.route("/login")
def login():
    google = oauth.create_client("google")
    redirect_uri = url_for("authorize", _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route("/authorize")
def authorize():
    google = oauth.create_client("google")
    token = google.authorize_access_token()
    resp = google.get("userinfo", token=token)
    user_info = resp.json()
    session["email"] = user_info["email"]
    return redirect("/")




@app.route("/logout")
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return render_template("success.html")

#___________________________________________________________________________________

if __name__ == "__main__":
    app.run(debug=True)