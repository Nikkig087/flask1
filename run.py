import os
import json
from flask import Flask, render_template, request, flash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)  
#app is default, this is an instance of the flask class
#name is our module
app.secret_key = os.environ.get("SECRET_KEY")


#route tells Flask what URL should triger the function that follows

#@ shows its a decorator, this wraps functions(objects)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    data = []
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
    return render_template("about.html",page_title="About",company=data) #new varible called company which will be sent to the html template which is equal to the json_data its loading from the json_data file


@app.route('/about/<member_name>') #this will pass in our name to the view below
def about_member(member_name):
    member= {}
    with open("data/company.json","r") as json_data:
        data = json.load(json_data) # this converts the data inside into json
        for obj in data:
            if obj["url"]== member_name:
                member=obj
    return render_template("member.html", member=member) #this first member is the varible being passed through into our html file, second member is the member object we created here on line 29


@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method == "POST":
         flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
            
             #as this returns a dict we can pull the name info out of it, if form did not have key of Name = this would return None
             
       # print(request.form["email"]) # if email did not exsist we would get an exception
    return render_template("contact.html",page_title="Contact")

@app.route("/careers")
def careers():
    return render_template("careers.html",page_title="Careers")



if __name__ == "__main__": # then run with following arguments
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),#casting as int
        debug=True)# only have this in dev never have it true when submitting project