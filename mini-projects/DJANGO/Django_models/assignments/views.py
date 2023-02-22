from audioop import reverse
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Assignment
from .forms import AssignmentForm
from django.utils import timezone

# Create your views here.
def index(request):
    assignments = Assignment.objects.all().order_by('date_due')

    date = timezone.now()
    context = {
        'assignments': assignments,
        'date':date
    }

    return render(request, 'assignments/index.html', context)

def create(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            #form.save()
            assignment = Assignment()
            assignment.title = form.cleaned_data['title']
            assignment.description = form.cleaned_data['description']   
            date_assigned = form.cleaned_data['date_assigned']
            date_due = form.cleaned_data['date_due']

            if date_assigned:
                assignment.date_assigned = date_assigned
            if date_due:
                assignment.date_due = date_due
            assignment.save()
            return HttpResponseRedirect(reverse('assignment:index'))
        else:
            context = {
                'form': form,
            } 
            return render(request, 'assignments/create.html', context)
    context = {
        'form': AssignmentForm,
    }

    return render(request, 'assignments/create.html', context)
