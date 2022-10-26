from dataclasses import fields
from importlib.metadata import MetadataPathFinder
from tkinter import Widget
from django import forms
from django.forms import SelectDateWidget
from demoapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime

class LoginForm(forms.Form):
    name = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password')

class StudentForm(forms.Form):
    name = forms.CharField(label='name', max_length=50)
    roll_no = forms.IntegerField(label='Roll no')
    class_no = forms.IntegerField(label='class no')
    address = forms.CharField(label='Address', max_length=70)
 
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employees 
        fields = "__all__"  

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'name', 'description']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__' 

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'
        
class QuizModelForm(forms.ModelForm):
    class Meta:
        model = QuizModel
        fields = '__all__'