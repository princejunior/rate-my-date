from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
# Authentication models and functions
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from fire.fireconfig import Firebase  # Assuming this is your Firebase configuration
from .models import Person, Post, Comment  # Importing your models
from .forms import PostForm, CreateUserForm, LoginForm, PersonForm  # Importing forms

# SEARCH 
from django.db.models import Q  # Importing Q object for complex queries
# time
from datetime import datetime
from django.utils import timezone
from django.contrib import messages  # Importing messages framework for displaying messages to users

import logging
logger = logging.getLogger(__name__)
# Create your views here.

def home(request):
    # Fetch most recent posts ordered by creation date
    recent_posts = Post.objects.order_by('-created_at')
    
    context = {
        'user': request.user,  # Pass the user object to the context
        'recent_posts': recent_posts  # Pass recent posts to the context
    }
    return render(request, 'pages/home.html', context=context)

# Placeholder function for handling comments
def comment(request):
    # Your logic here
    pass

# Renders the page for creating a new person profile
def createNewPerson(request):
    context = {
        'user': request.user  # Pass the user object to the context
    }
    return render(request, 'create/createnewperson.html', context=context)

# View function for viewing a person's profile
@login_required
def view_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    recent_posts = Post.objects.filter(person=person).order_by('-created_at')
    
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            # Process form data when submitted
            post = post_form.save(commit=False)
            post.person = person
            post.user = request.user
            post.save()
            messages.success(request, 'Post submitted successfully.')
            return redirect('viewperson', person_id=person_id)
        else:
            # Display form errors if form is invalid
            messages.error(request, 'Failed to submit post. Please check the form.')
    else:
        post_form = PostForm()
        
    context = {
        'user': request.user,
        'person': person,
        'post_form': post_form,
        'recent_posts': recent_posts
    }
    return render(request, 'pages/view_person.html', context=context)

# Handles adding comments to posts
@login_required
def add_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        comment_text = request.POST.get('comment')
        post = get_object_or_404(Post, pk=post_id)
        # Create the comment
        comment = Comment(post=post, user=request.user, text=comment_text)
        comment.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# Renders the search results page based on user queries
def searchPerson(request):
    query = request.GET.get('query')
    results = []

    if query:
        # Perform search operation
        results = Person.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(instagram__icontains=query))

    context = {
        'user': request.user,
        'results': results,
        'query': query
    }
    return render(request, 'pages/search_results.html', context=context)

# Renders the explore page, displaying all available person profiles
def explore(request):
    persons = Person.objects.all()
    context = {
        'user': request.user,  # Pass the user object to the context
        'persons': persons,
    }
    return render(request, 'pages/explore.html', context=context)

# CREATE A PERSON
@login_required
def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.user = request.user
            
            # Set joined_date to the current date
            current_date = timezone.now().strftime('%Y-%m-%d')
            person.joined_date = current_date
            
            person.save()
            return redirect('viewperson', person_id=person.id)
    else:
        form = PersonForm()
    
    return render(request, 'create_person.html', {'form': form, 'current_date': timezone.now().strftime('%Y-%m-%d')})

# Handles the creation of a new post associated with a person profile
@login_required
def create_post(request, person_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Create a new post instance but don't save it yet
            post = form.save(commit=False)
            # Assign the user and person IDs to the post instance
            post.user_id = request.user.id
            post.person_id = person_id
            # Now save the post instance
            post.save()
            return redirect('view_person', person_id=person_id)
    else:
        form = PostForm()
    return render(request, 'create/create_post.html', {'form': form})

# Increments the agree count for a specific comment
def agree_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.agree += 1
    comment.save()
    return redirect('post_detail', post_id=comment.post_id)

# AUTHENTICATION

# Handles user registration
def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
    
    context ={ 'registerform': form}
    
    return render(request, 'auth/signup.html', context = context)

# Handles user login
def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("/")
            else:
                print("Failed to authenticate user")

    context = {'loginform': form, 'user': request.user}
    return render(request, 'auth/ogin.html', context=context)

# Logs out the current user
def user_logout(request) :
    auth_logout(request)  
    return redirect('/')

# Renders the dashboard page
@login_required(login_url="my-login")
def dashboard(request):
    return render(request, 'create/createnewperson.html')
