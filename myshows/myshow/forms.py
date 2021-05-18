from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating")

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)