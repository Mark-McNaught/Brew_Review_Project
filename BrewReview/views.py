from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from BrewReview.forms import UserForm, UserProfileForm


def index(request):
    context_dict = {'boldmessage': 'Testing view and index template'}
    return render(request, 'BrewReview/index.html', context=context_dict)

def map(request):
    return render(request, 'BrewReview/map.html')

def shops(request):
    return HttpResponse("shops page goes here")

def profile(request):
    context_dict = {}
    return render(request, 'BrewReview/profile.html', context=context_dict)


def account_settings(request):
    context_dict = {}
    return render(request, 'BrewReview/account_settings.html', context=context_dict)



def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'BrewReview/signup.html', context={'user_form': user_form,
                                                           'profile_form': profile_form,
                                                           'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('BrewReview:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'BrewReview/login.html')

def settings(request):
    return HttpResponse("user settings page goes here")