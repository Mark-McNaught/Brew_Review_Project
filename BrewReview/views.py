from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse

from BrewReview.forms import UserForm, UserProfileForm, CoffeeShopForm
from BrewReview.models import CoffeeShop, Review, Addresses

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
            lat = result.get("lat")
            lng = result.get("lng")
            coffee_shop.address.lat = lat
            coffee_shop.address.lng = lng
            coffee_shop.address.save()
            lat_list += ","+str(lat)
            lng_list += ","+str(lng)
        else:
            lat_list += ","+str(coffee_shop.address.lat)
            lng_list += ","+str(coffee_shop.address.lng)

       # addresses += "!"+coffee_shop.address.address_line_1+", "+coffee_shop.address.postcode+", "+coffee_shop.address.city+", "+coffee_shop.address.country
    context_dict = {'shops': coffee_shop_list, 'length': length, 'names': names, 'lat_list': lat_list, 'lng_list': lng_list }
    return render(request, 'BrewReview/map.html', context=context_dict)

def shops(request):
    shops = CoffeeShop.objects.all()
    context_dict = {'navbar_active':'shops', 'shops':shops}
    return render(request, 'BrewReview/shops.html', context=context_dict)

def show_shop(request, shop_slug):
    context = {}
    try:
        shop = CoffeeShop.objects.get(slug=shop_slug)
        reviews = Review.objects.filter(coffee_shop=shop)
        context['reviews'] = reviews
        context['shop'] = shop
    except CoffeeShop.DoesNotExist:
        context['shop'] = None
        context['reviews'] = None
    return render(request, 'BrewReview/shop.html', context=context)

def add_shop(request):
    form = CoffeeShopForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CoffeeShopForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/BrewReview/')
        else:
            print(form.errors)
    return render(request, 'BrewReview/add_shop.html', {'form': form})



def searched(request):
    context_dict = {'navbar':'shops'}
    if request.method == 'POST':
        search = request.POST.get('search', '')
        shops = CoffeeShop.objects.filter(name__contains=search)
        return render(request, 'BrewReview/searched.html', {'search':search, 'shops':shops, 'context':context_dict})
    else:
        return render(request, 'BrewReview/searched.html', context=context_dict)


@login_required
def account_settings(request):
    context_dict = {'navbar_active':'settings'}
    return render(request, 'BrewReview/account_settings.html', context=context_dict)


@login_required
def profile(request):
    context_dict = {'navbar_active':'profile'}
    return render(request, 'BrewReview/profile.html', context=context_dict)



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



def user_logout(request):
    logout(request)
    return redirect(reverse('BrewReview:index'))