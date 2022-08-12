from flask import Flask, request, render_template, redirect

app = Flask(__name__)

todo_list = [{"text": "Make a todo list", "priority": "high", "complete": False}]

@app.route("/", methods=['GET','POST'])
def index():
    todo=request.form.get("todo_text")
    priority = request.form.get("todo_priority")
    
    
    if todo:
        todo_list.append({"text":todo,  "priority":priority, "complete":False})
    
    return render_template("index.html", todo_list=todo_list)

@app.route('/complete/<int>:index')
def completetodo(index):
    todo_list[index]["complete"] = not todo_list[index]["complete"]

    return redirect("/")

@app.route("/delete/<int>:index")
def delete_todo(index):
    todo_list.pop(todo_list[index])

    return redirect("/")

app.run(debug=True)