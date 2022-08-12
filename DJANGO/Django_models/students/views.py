from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from assignments.models import Assignment

# Create your views here.
from .models import Students

def index(request):
    students = Students.objects.all()

    context = {
        "students": students
    }

    return render(request, 'students/index.html', context)

def detail(request, student_id):
    try:
        student = Students.objects.get(id=student_id)
    except Students.DoesNotExist:
        return HttpResponseRedirect(reverse('students:index'))
    
    assignments = Assignment.objects.all()
    context = { 
        'student': student,
        'assignments': assignments
    }

    return render(request, 'students/detail.html', context)

def update(request):
    if request.method == "POST":
        form = request.POST
        assignment_id = form.get('assignment')
        student_id =form.get('student')
        try:
            student = Students.objects.get(id=student_id)
            assignment = Assignment.objects.get(id=assignment_id)
        except (student.DoesNotExist, assignment.DoesNotExist):
            return HttpResponseRedirect(reverse('students:index'))
        student.assignments.add(assignment)   

        student.save()

        return HttpResponseRedirect(reverse('students:details', args= student_id))

    


