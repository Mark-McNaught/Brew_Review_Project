from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from BrewReview.forms import UserForm, UserProfileForm
from BrewReview.models import CoffeeShop
import googlemaps


def index(request):
    context_dict = {'boldmessage': 'Testing view and index template', 'navbar_active':'home'}
    return render(request, 'BrewReview/index.html', context=context_dict)

def map(request):
    gmaps = googlemaps.Client(key="AIzaSyDDv5ekhgkSI-hTpzWp8bXYwxrP0D8IBjQ")
    coffee_shop_list = CoffeeShop.objects.all()
    length = len(coffee_shop_list)
    names = coffee_shop_list[0].name
    result =gmaps.geocode(coffee_shop_list[0].address.address_line_1 + ", " + coffee_shop_list[0].address.postcode + ", " +
                  coffee_shop_list[0].address.city + ", " + coffee_shop_list[0].address.country)[0].get("geometry",None).get("location",None)
    lat_list = str(result.get("lat"))
    lng_list = str(result.get("lng"))
   # addresses=""
    for coffee_shop in coffee_shop_list[1:]:
        names += ", " + coffee_shop.name
        if coffee_shop.address.lat is None and coffee_shop.address.lat is None:
            result = (gmaps.geocode(coffee_shop.address.address_line_1 + ", " + coffee_shop.address.postcode + ", " +
            coffee_shop.address.city + ", " + coffee_shop.address.country)[0]
                      .get("geometry", None).get("location", None))
            lat_list += ","+str(result.get("lat"))
            lng_list += ","+str(result.get("lng"))
        else:
            lat_list += ","+str(coffee_shop.address.lat)
            lng_list += ","+str(coffee_shop.address.lng)

       # addresses += "!"+coffee_shop.address.address_line_1+", "+coffee_shop.address.postcode+", "+coffee_shop.address.city+", "+coffee_shop.address.country


    context_dict = {'shops': coffee_shop_list, 'length': length, 'names': names, 'lat_list': lat_list, 'lng_list': lng_list }
    return render(request, 'BrewReview/map.html', context=context_dict)

def shops(request):
    return HttpResponse("shops page goes here")

@login_required
def profile(request):
    context_dict = {'navbar_active':'profile'}
    return render(request, 'BrewReview/profile.html', context=context_dict)


def account_settings(request):
    context_dict = {'navbar_active':'profile'}
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

def user_settings(request):
    return render(request, 'BrewReview/user_settings.html')

def user_logout(request):
    logout(request)
    return redirect(reverse('BrewReview:index'))