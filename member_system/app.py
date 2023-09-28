# initialize database connection
import pymongo
client=pymongo.MongoClient("mongodb+srv://root:root123@kaicluster.f9neu2k.mongodb.net/?retryWrites=true&w=majority")
db=client.member.member_system
print("Database initialized successfully!")

# initialize Flask server
from flask import *
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)

app.secret_key="any string but secret"

# handle router
@app.route("/")
def index():
    return render_template("index.html")

# member page
@app.route("/member")
def member():
    if "name" in session:
        return render_template("member.html")
    else:
        return redirect("/")

# error
# /error?msg=error message
# /error?msg=wrong password
@app.route("/error")
def error():
    message=request.args.get("msg", "Error occur, please contact us via email.")
    return render_template("error.html", message=message)

# signup
@app.route("/signup", methods=["POST"])
def signup():

    # receive data from front end
    name=request.form["username"]
    email=request.form["email"]
    password=request.form["password"]
    print("Username: ", name)
    print("Email: ", email)
    print("Password: ", password)

    # connect with database
    collection=db.user
    # check if there's repeating email 
    result=collection.find_one({
        "Email":email
    })
    if result != None:
        return redirect("error?msg=Account already registered.")
    # store data in database and complete registration
    collection.insert_one({
        "Username": name,
        "Email": email,
        "Password": password
    })
    return redirect("/")

# signin
@app.route("/signin", methods=["POST"])
def signin():

    # receive data from front end
    email=request.form["email"]
    password=request.form["password"]
    print("Email: ", email)
    print("Password: ", password)

    # connect with database
    collection=db.user
    # check if username and password are correct
    result=collection.find_one({
        "$and":[
            {"Email":email},
            {"Password":password}
        ]
    })
    # redirect to error page, if username or password is not correct
    if result == None:
        return redirect("error?msg=Username or password is incorrect.")
    # if login successfully, Session record the current user infromation
    print(result)
    session["name"]=result["Username"]
    # login successfully, redirect to member page
    return redirect("/member")

# sign out
@app.route("/signout")
def signout():

    # delete the Session's current user information
    del session["name"]
    return redirect("/")

app.run(port=300)