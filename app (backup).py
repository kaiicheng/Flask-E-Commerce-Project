from flask import Flask
from flask import request
from flask import redirect  # redirect to a address
from flask import render_template  # template engine 
import json

# build a application object
app =  Flask(
    __name__,
    static_folder="public",  # static folder
    static_url_path="/"  # static folder path (if set as "/abc", then test.txt file can be found on "/abc/test.txt")
    )

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
    return json.dumps({
        "status": "沒問題.",
        "text": "您好 Flask!"
    }, ensure_ascii=False)  # not use ASCII to interpret Chinese (zh-TW)


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

# boost web server, can assign port number
# app.run()
app.run(port=3000)