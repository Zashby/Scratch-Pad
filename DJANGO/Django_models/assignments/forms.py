from .models import Assignment
from django import forms

class AssignmentForm(forms.ModelForm):
     class Meta: 
         model = Assignment
         exclude = ()
         widgets = {
            'date_assigned': forms.widgets.DateInput(attrs={'type': 'date'}),
            'date_due': forms.widgets.DateInput(attrs={'type': 'date'})
        }
# class AssignmentForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     #description = forms.TextField()
#     date_assigned =     holiday_date = forms.DateField(widget=forms.TextInput(attrs=
#                                 {
#                                     'class':'datepicker'
#                                 }))
#     date_due = forms.DateField()
