from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.forms import ModelForm


# class SignUpForm(UserCreationForm):
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ['username','first_name', 'last_name', 'email', 'password1']
#         labels = {'email':'Email'}
#         help_texts = {
#             'username': None,
#             'password1': None,
#         }

class AddListForm(ModelForm):
    # date = forms.DateField(label='Date',input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Task
        fields = ['title', 'description','date', 'complete']