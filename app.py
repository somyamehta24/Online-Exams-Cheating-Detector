from flask import Flask, render_template, request, url_for, redirect, session
from data.question1 import detector1
from data.question2 import detector2
import yaml, os
from authlib.integrations.flask_client import OAuth
app = Flask(__name__)


os.chdir("D:/OECD")
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

    return render_template("Frontend.html")

@app.route('/start')
def start():
    email = dict(session).get("email", None)

    if(email == None):
        return redirect("/login")

    return render_template("index.html", email=email)

@app.route('/instructions')
def instructions():
    return render_template("instructions.html")

@app.route("/submit", methods=['POST'])
def submit():
    email = dict(session).get("email", None)

    if(email == None):
        return redirect("/login")

    if(request.method == "POST"):
        
        answers = request.form
        
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

@app.route("/admin")
def admin():
    email = dict(session).get("email", None)

    if(email == None):
        print("/login")
        return redirect("/login")
    
    elif email == "garvitgalgat@gmail.com":
        li1 = detector1.printdata()
        li2 = detector2.printdata()
        
        q1 = []
        q2 = []
        
        for item in li1:
            if item[2] > 0.75:
                tup = (item[0], item[1], item[2]*100)
                q1.append(tup)

        
        for item in li2:
            if item[2] > 0.75:
                tup = (item[0], item[1], item[2]*100)
                q2.append(tup)
           
        q3=sorted(q1, key = lambda element : element[2], reverse=True)
        q4=sorted(q2, key = lambda element : element[2], reverse=True)
            
            
        return render_template("tables.html",q1=q3, q2=q4)
    
    else:
        return render_template("error.html")

@app.route("/admin/<ques>/<email>")
def answer(ques, email):
    user = dict(session).get("email", None)
    
    if(user != "garvitgalgat@gmail.com"):
        return render_template("error.html")
    print(ques, email)
    ext = ""
    if(ques == "question1"):
        ext = "1.txt"
    elif(ques == "question2"):
        ext = "2.txt"
    else:
        return render_template("error.html")
    
    # print(os.getcwd())
    path = "D:\\OECD"+ "\data\\"+ques+"\\"+email+ext
    print(path)
    # print(path)
    f1 = open(path, "r")
    s = f1.read()
    return render_template('submission.html',data=s,email=email)

    


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
    email = str(session["email"])

    if(email == "garvitgalgat@gmail.com"):
        return redirect("/admin")

    f1 = open("data/students.txt", "r")
    s = f1.read()
    email = str(session["email"])
    if s.find(email) == -1:

        f1 = open("data/students.txt", "a")
        f1.write(session["email"]+ " ")
        f1.close()


        return redirect("/start")
    
    else:
        for key in list(session.keys()):
            session.pop(key)
        return render_template("already.html")




@app.route("/logout")
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return render_template("success.html")

#___________________________________________________________________________________

@app.errorhandler(Exception)
def all_exception_handler(error):
   return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)