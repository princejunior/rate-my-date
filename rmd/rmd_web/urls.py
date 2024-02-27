from django.urls import path
from . import views

urlpatterns = [
    # GET requests
    path('', views.home, name='home'),  # Route for the home page
    path('person/', views.createNewPerson, name='createnewperson'),  # Route for creating a new person profile
    path('search/', views.searchPerson, name='searchperson'),  # Route for searching persons
    path('explore/', views.explore, name='explore'),  # Route for exploring persons
    
    # Routes related to persons/dates
    path('create_person/', views.create_person, name='create_person'),  # Route for creating a new person profile
    path('viewperson/', views.view_person, name='viewperson'),  # Route for viewing a person's profile
    path('viewperson/<int:person_id>/', views.view_person, name='viewperson'),  # Route for viewing a person's profile by ID
    path('create_post/<int:person_id>/', views.create_post, name='create_post'),  # Route for creating a new post associated with a person
    path('add_comment/', views.add_comment, name='add_comment'),  # Route for adding a comment to a post
    
    # POST requests (These seem to be missing from your current implementation)
    
    # Authentication routes
    path('register/', views.register, name='signup'),  # Route for user registration
    path('my-login/', views.my_login, name='my-login'),  # Route for user login
    path('user-logout', views.user_logout, name="user-logout"),  # Route for user logout
]
