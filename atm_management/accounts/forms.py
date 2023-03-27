# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=250)

    password1 = forms.CharField(max_length=150,widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=150,widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')



