import os
from flask import Flask


app = Flask(__name__)  
#app is default, this is an instance of the flask class
#name is our module



#route tells Flask what URL should triger the function that follows

#@ shows its a decorator, this wraps functions(objects)
@app.route("/")
def index():
    return "Hello, World"


if __name__ == "__main__": # then run with following arguments
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),#casting as int
        debug=True)