from turtle import title
from django import forms
from .models import TodoItem

class AuthForm(forms.Form):
    username = forms.CharField(max_length=12, label='username')
    password = forms.CharField(max_length=12, label='password' , widget=forms.PasswordInput, )


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        exclude = ('date_created', 'date_completed', 'user')