from django import forms

choices = [("high", 'High'),('medium', 'Medium'),('low', 'Low')]

class TodoForm(forms.Form):

    todo_text = forms.CharField(label='Enter todo text:')
    priority = forms.ChoiceField(label='Priority:', choices=choices)
    