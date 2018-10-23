from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class signupform(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    dob = forms.DateField()
    email = forms.EmailField(max_length=250)
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2','dob','age')
