from flask import Flask, request, render_template
import string
import random

app=Flask(__name__)
#Input methods for GET and POST if using POST method of retrieving data from index
@app.route('/', methods=["GET", "POST"])
def index():
    #change args to form if drawing from HTML form
    username = request.form.get("name", "")
    try:
        pw_length = request.form.get("length", "0")
        password=""
        for x in range(int(pw_length)):
            password += random.choice(string.ascii_lowercase)
    except (ValueError, TypeError):
        return render_template("index.html", name=username, password="invalid, please input a whole number")
    
    print(password)
    #Put HTML file in "templates" folder if rendering template for flask
    
    return render_template("index.html", name=username, password=password)

@app.route("/logic")
def flask_logic():
    fruits = ['apple', 'banana', 'watermelon','strawberry','kiwi']
    users=[{'name':"bob", 'color':'red','age':25},{'name':"charles", 'color':'red','age':25},{'name':"john", 'color':'purple','age':28},{'name':"Mary", 'color':'blue','age':25}]
    
    temp=80

    return render_template("logic.html", fruits=fruits, users=users, temp=temp)

app.run(debug=True)
