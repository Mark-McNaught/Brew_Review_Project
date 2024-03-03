from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': 'Testing view and index template'}
    return render(request, 'BrewReview/index.html', context=context_dict)

def map(request):
    return HttpResponse("Map page goes here")

def shops(request):
    return HttpResponse("shops page goes here")

def profile(request):
    return HttpResponse("user profile page goes here, with link to user settings page")

def signup(request):
    return HttpResponse("sign up page goes here")

def settings(request):
    return HttpResponse("user settings page goes here")