from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import TodoForm

# Create your views here.
todos = []



def index(request): 
    
    if request.method == "POST":
        form =TodoForm(request.POST)
        #implemented error checking to prevent workarounds
        if form.is_valid():
            todo_item = request.POST.get('todo_text', "")
            priority = request.POST.get('priority', "low")
            todos.append({"todo_item": todo_item, "priority": priority, "complete": False })
        else:
            context = {'todos':todos, 'form':form}

    context = {"todos":todos, 'form':TodoForm(),}

    return render(request, 'todo_list/index.html', context)

def delete_todo(request, index):
    if abs(index) >= len(todos):
        return HttpResponse("no")
    todos.pop(abs(index))
    return HttpResponseRedirect('/todo')

def complete_todo(request, index):
    index= abs(index)
    if index >= len(todos):
        return HttpResponse("no")
    todos[index]['complete'] = not todos[index]['complete']
    return HttpResponseRedirect('/todo')