# Django Forms Module
from django import forms
#Django Built-in Users Module
from django.contrib.auth.models import User
#Django Built-in Users Form Creator
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm (UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
