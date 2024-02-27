# forms.py
from .models import Post, Comment, Person  # Importing models
from django import forms  # Importing Django forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Importing forms for user registration and authentication
from django.contrib.auth.models import User  # Importing User model from Django's authentication system
from django.forms.widgets import PasswordInput, TextInput  # Importing widgets for form fields

# Creates a form for adding a post for the date
class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Specifies the model to use
        fields = ['content', 'how_met']  # Specifies the fields to include in the form

# Creates a form for adding a profile for the date 
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person  # Specifies the model to use
        fields = ['first_name', 'last_name', 'instagram', 'joined_date']  # Specifies the fields to include in the form
        widgets = {
            'joined_date': forms.DateInput(attrs={'type': 'date'}),  # Specifies the widget for the joined_date field
        }
        required = {
            'joined_date': False,  # Makes joined_date field optional
        }

# Form for registering a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User  # Specifies the model to use
        fields = ['username', 'email', 'password1', 'password2']  # Specifies the fields to include in the form
        widgets = {
            'password': forms.PasswordInput()  # Specifies the widget for the password field
        } 
        
# Form for authenticating a User
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())  # Specifies the widget for the username field
    password = forms.CharField(widget=TextInput())  # Specifies the widget for the password field
