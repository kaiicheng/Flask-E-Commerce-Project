from flask import Flask
from flask import request
from flask import redirect  # redirect to router "/..."
from flask import render_template  # template engine to call file under templates folder
from flask import session
import json

# build a application object, set static file path
# http://127.0.0.1:3000/Temple.JPG
app =  Flask(
    __name__,
    static_folder="public",  # static folder
    static_url_path="/"  # static folder path (if set as "/abc", then test.txt file can be found on "/abc/test.txt")
    )

# Session
# need to set private key for session before using session
app.secret_key="any string but secret"

# Query String 
# create path "/getSum", respone from the getSum(): /getSum?max=maximal number (/getSum?max=5)
# getSum(): /getSum?min=minimal number&max=maximal number (/getSum?min=2&max=5)
@app.route("/getSum")
def getSum():  # 1+2+3+...+100
    # get parameter
    maxNumber=request.args.get("max", 100)  # if no "max" argument, default 100
    maxNumber=int(maxNumber)
    print("Maximal number: ", maxNumber)

    minNumber=request.args.get("min", 1)  # if no "min" argument, default 1
    minNumber=int(minNumber)
    print("Minimal number: ", minNumber)

    result = 0
    for n in range(minNumber, maxNumber+1):
        result+=n
    return "Sum: " + str(result)

# Form
# create path "/testget"
# use GET method to handle /testget
@app.route("/testget", methods=["GET"])
def testGet():
    # get input data from front end
    name=request.args.get("n", "")
    return "Welcome " + name

# Form
# create path "/testpost"
# use POST method to handle /testpost
@app.route("/testpost", methods=["POST"])
def testPost():
    # # get input data from front end
    # # GET method to receive Query String
    # maxNumber=request.args.get("max", "")
    
    # POST method to receive Query String
    maxNumber=request.form["max"]
    maxNumber=int(maxNumber)
    # 1+2+...+maxNumber
    result=0
    for n in range(1, maxNumber+1):
        result+=n
    
    # use template engine to call result from result.html under templates folder
    # return "Result: " + str(result)
    return render_template("result.html", data=result)

# Form
# create path "/show"
@app.route("/show")
def show():
    # get input data from front end
    name=request.args.get("n", "")
    return "Welcome " + name

# Form
# create path "/calculate"
@app.route("/calculate")
def calculate():
    # get input data from front end
    maxNumber=request.args.get("max", "")
    maxNumber=int(maxNumber)
    # 1+2+...+maxNumber
    result=0
    for n in range(1, maxNumber+1):
        result+=n
    
    # use template engine to call result from result.html under templates folder
    # return "Result: " + str(result)
    return render_template("result.html", data=result)

# first website
# create path "/", respone from the homepage of website
@app.route("/")
def index():  # function to response and handle path "/"
    # request information
    # print("----------")
    
    # print("Request method: ", request.method)
    # print("Request scheme: ", request.scheme)
    # print("Request host: ", request.host)
    # print("Request path: ", request.path)
    # print("Request url: ", request.url)
    # print("----------")
    
    print("Browser and Operating System: ", request.headers.get("user-agent"))
    print("Request url: ", request.headers.get("accept-language"))
    print("Request url: ", request.headers.get("referrer"))
    print("----------")

    # redirect
    # return redirect("https://www.google.com/")

    # To test default language for browser
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        # return "Hello Flask!"

        # redirect
        return redirect("/en/")
       
        # # response
        # # return json format from dictionary
        # return json.dumps({
        #     "status": "Ok.",
        #     "text": "Hello World!"
        # })
    else:
        # return redirect("/en/")

        # redirect
        return redirect("/zh/")
       
        # # return "您好 Flask!"
        # # return json format from dictionary
        # return json.dumps({
        #     "status": "沒問題.",
        #     "text": "您好 Flask!"
        # }, ensure_ascii=False)  # not use ASCII to interpret Chinese (zh-TW)
    
    # return "Hello Flask!"

# second website
# create path "/page", respone from the page()
@app.route("/page")
def page():  # response to path "/page"
    return render_template("page.html")

# create path "/en/", respone from the index_english()
@app.route("/en/")
def index_english():  # response to path "/en/"
    return json.dumps({
        "status": "Ok.",
        "text": "Hello World!"
    })

# create path "/zj/", respone from the index_chinese()
@app.route("/zh/")
def index_chinese():  # response to path "/zh"

    # return json.dumps({
    #     "status": "沒問題.",
    #     "text": "您好 Flask!"
    # }, ensure_ascii=False)  # not use ASCII to interpret Chinese (zh-TW)

    # # use template engine to return index file under templates folder
    # # so it's easier to manage text content file (such as adding html) under templates folder
    # return render_template("index", name="Kai")  # default name="Kai"

    # move html scripts to index.html file under templates folder
    # return "<!DOCTYPE html><html>Hello Flaks</html>"
    return render_template("index.html")

# create path "/data", respone from the handleData()
@app.route("/data")
def handleData():  # response to path "/data"
    return "My data."

# dynamic routing
# create path "/user", respone from the handleUser()
@app.route("/user/<username>")
def handleUser(username):  # response to path "/user"
    if username=="Kai":
        return "Welcome back " + username + "!"
    else:
        return "Hello " + username + "!"

# Session
# use GET method to handle path /hello?name=user name
@app.route("/hello")
def hello():
    name=request.args.get("name", "")
    session["username"]=name  # session["...name..."]=data
    return "Hello "+name

# Session
# get name stored in the session via hello()
# use GET method to handle path /talk
@app.route("/talk")
def talk():
    name=session["username"]
    # return "Who are you?"
    return "Welcome back "+name+"!"

if __name__ == "__main__":
    app.run(port=3000)