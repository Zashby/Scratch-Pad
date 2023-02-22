from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone


from .models import Priority, TodoItem

from .forms import AuthForm, TodoForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    context = {
        'form': AuthForm()
    }

    if request.method=='POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            #create_user saves data input
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'],)
            auth.login(request, user)
            return render(request, 'todo/signup.html')
        else:
            context = {'form' : form,}
            pass

    return render(request, 'todo/signup.html', context)



def login(request):
    context = {
        'form': AuthForm(),
    }
    if request.method == 'POST':
        form=AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username = username, password=password)
            if user != None:
                auth.login(request, user)
                next = request.GET.get('next')
                if next:
                    return redirect(next)
                    
                return redirect('todo:index')

        form.add_error(error='invalid username or password', field='username')    
        context['form'] = form
        return render(request, 'todo/login.html', context)


    return render(request, 'todo/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('todo:index')




@login_required(login_url='todo:index')
def index(request):
    
        completed_todos = TodoItem.objects.filter(user=request.user, date_completed__isnull=False)
        todos = TodoItem.objects.filter(user=request.user, date_completed__isnull=True)
        context = {
        'todos': todos, 'form': TodoForm(), 'completed':completed_todos,
        }
        return render(request, 'todo/index.html', context)

@login_required(login_url='todo:login')
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_item =TodoItem()
            todo_item.text = form.cleaned_data['text']
            todo_item.priority = form.cleaned_data['priority']
            todo_item.user = request.user
            todo_item.save()
    return redirect('todo:index')


def delete(request, todo_id):
    try:
        todo = TodoItem.objects.get(id=todo_id)
        if todo.user == request.user:
            todo.delete()
    except TodoItem.DoesNotExist:
        pass
    return redirect('todo:index')

def update(request, todo_id):
    if request.method =='GET':
        try:
            todo = TodoItem.objects.get(id=todo_id)
            if todo.user == request.user:
                context = {
                    'todo':todo,
                    'form':TodoForm(instance=todo)
                }
                return render(request, 'todo/update.html' ,context)

        except TodoItem.DoesNotExist:
            return redirect('todo:index')
    elif request.method == 'POST':
        try:
            todo = TodoItem.objects.get(id=todo_id)
        except TodoItem.DoesNotExist:
            pass

        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('todo:index')

def complete(request, todo_id):
    try:
        todo = TodoItem.objects.get(id=todo_id)

    except TodoItem.DoesNotExist:
        # TODO: create 404 page
        pass

    todo.date_completed = timezone.now()
    todo.save()
    return redirect('todo:index')