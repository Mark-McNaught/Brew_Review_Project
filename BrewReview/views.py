from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

#from django.conf import settings

from BrewReview.forms import UserForm, UserProfileForm, CoffeeShopForm, ReviewForm
from BrewReview.models import CoffeeShop, Review, UserProfile

import googlemaps


def index(request):
    recent_reviews = Review.objects.order_by('-date')[:6]  # Fetch the 4 most recent reviews
    for review in recent_reviews:
        shop_name = CoffeeShop.objects.get(pk=review.coffee_shop_id).name
        slug = CoffeeShop.objects.get(pk=review.coffee_shop_id).slug
        review.shop_name = shop_name
        review.shop_slug = slug
    return render(request, 'BrewReview/index.html', {'recent_reviews': recent_reviews})


def get_recent_reviews(request):
    recent_reviews = Review.objects.order_by('-date')[:6]
    reviews_data = []
    for review in recent_reviews:
        review_data = {
            'title': review.title,
            'user': review.user.username,
            'shop_name': review.coffee_shop.name,
            'rating': review.rating,
            'shop_slug': review.coffee_shop.slug
        }
        reviews_data.append(review_data)
    return JsonResponse({'recent_reviews': reviews_data})

def map(request):
    gmaps = googlemaps.Client(key="AIzaSyDDv5ekhgkSI-hTpzWp8bXYwxrP0D8IBjQ")
    coffee_shop_list = CoffeeShop.objects.all()
    length = len(coffee_shop_list)
    names = coffee_shop_list[0].name
    lat_list = str(coffee_shop_list[0].lat)
    lng_list = str(coffee_shop_list[0].lng)
    url_list = str(coffee_shop_list[0].slug)
    for coffee_shop in coffee_shop_list[1:]:
        names += ", " + coffee_shop.name
        lat_list += ","+str(coffee_shop.lat)
        lng_list += ","+str(coffee_shop.lng)
        url_list += ","+str(coffee_shop.slug)

    # addresses += "!"+coffee_shop.address.address_line_1+", "+coffee_shop.address.postcode+", "+coffee_shop.address.city+", "+coffee_shop.address.country
    context_dict = {'shops': coffee_shop_list, 'length': length, 'names': names, 'lat_list': lat_list, 'lng_list': lng_list, 'url_list': url_list }
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
    gmaps = googlemaps.Client(key="AIzaSyDDv5ekhgkSI-hTpzWp8bXYwxrP0D8IBjQ")
    form = CoffeeShopForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CoffeeShopForm(request.POST)
        if form.is_valid():
            shop = form.save(commit=True)
            address = (str(shop.address_line_1) + ", " + str(shop.postcode) + ", " +
                       str(shop.city) + ", " + str(shop.country))
            result = (gmaps.geocode(address)[0].get("geometry", None).get("location", None))
            if result:
                shop.lat = result.get("lat")
                shop.lng = result.get("lng")
                shop.save()
                return redirect('/BrewReview/')
            else:
                print("invalid address")
        else:
            print(form.errors)
    return render(request, 'BrewReview/add_shop.html', {'form': form})

@login_required
def add_review(request, shop_slug):
    try:
        shop = CoffeeShop.objects.get(slug=shop_slug)
    except CoffeeShop.DoesNotExist:
        shop = None

    if shop is None:
        return redirect('/BrewReview/')
    
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.coffee_shop = shop
            review.user = request.user
            review.save()

            return redirect(reverse('BrewReview:show_shop', kwargs={'shop_slug': shop_slug}))
        else:
            print(form.errors)
    return render(request, 'BrewReview/add_review.html', {'form': form, 'shop': shop})

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
