from django import forms
from . models import Task
from . models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user'] # user chara baki sob asbe
class LoginForm(forms.Form): 
    username = forms.CharField(max_length=150) 
    password = forms.CharField(widget=forms.PasswordInput)