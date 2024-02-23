# forms.py
from .models import Post, Comment, Person
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput   

# Creates a post for the date
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'person', 'content', 'how_met']

# Creates a Profile for the date 
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'instagram', 'joined_date']
        widgets = {
            'joined_date': forms.DateInput(attrs={'type': 'date'}),
        }
        # Make joined_date field optional
        required = {
            'joined_date': False,
        }

        
# Registe a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        # fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']
        widgets = {
            'password': forms.PasswordInput()
        } 
        
# Authenticate a User
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=TextInput())