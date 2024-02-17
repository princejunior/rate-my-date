from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from fire.fireconfig import Firebase

# Create your views here.

def home(request):
    # initFire = Firebase()
    # initFire.get_data()
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def comment():
    return

def createNewPerson(request):
    template = loader.get_template('createnewperson.html')
    return HttpResponse(template.render())
