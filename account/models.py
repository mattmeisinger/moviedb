from django.db import models
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField()

class CreateAccountForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.CharField()
    password = forms.CharField()
    verify_password = forms.CharField()
