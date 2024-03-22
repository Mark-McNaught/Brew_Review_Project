from django.contrib.auth.decorators import login_required

from django.db.models import Avg
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


from BrewReview.forms import CoffeeShopForm, ReviewForm, ChangeUsernameForm
from BrewReview.models import CoffeeShop, Review

import googlemaps


def index(request):
    try:
        recent_reviews = Review.objects.order_by('-date')[:6]  # Fetch the 4 most recent reviews
        for review in recent_reviews:
            shop_name = CoffeeShop.objects.get(pk=review.coffee_shop_id).name
            slug = CoffeeShop.objects.get(pk=review.coffee_shop_id).slug
            review.shop_name = shop_name
            review.shop_slug = slug
    except:
        recent_reviews = None
    return render(request, 'BrewReview/index.html', {'navbar_active':'home', 'recent_reviews': recent_reviews})


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

def map(request, center_lat=55.8724, center_lng=-4.2900, zoom=11):
    gmaps = googlemaps.Client(key="AIzaSyDDv5ekhgkSI-hTpzWp8bXYwxrP0D8IBjQ")
    filter_param = request.GET.get('filter', False)
    if filter_param == "on":
        filter_param = True
        coffee_shop_list = CoffeeShop.objects.filter(serves_food=True)
    else:
        filter_param = False
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
    context_dict = {'navbar_active':'map', 'length': length, 'names': names, 'lat_list': lat_list,
                    'lng_list': lng_list, 'url_list': url_list, 'center_lat':center_lat,
                    'center_lng':center_lng, 'zoom':zoom, 'shops':coffee_shop_list,
                    'filter_param':filter_param}
    return render(request, 'BrewReview/map.html', context=context_dict)

def shops(request):
    shops = CoffeeShop.objects.all()
    filter_param = request.GET.get('filter', False)
    if filter_param == "on":
        filter_param = True
        coffee_shop_list = CoffeeShop.objects.filter(serves_food=True)
    else:
        filter_param = False
        coffee_shop_list = CoffeeShop.objects.all()
    context_dict = {'navbar_active':'shops', 'shops':shops, 'filter_param':filter_param}
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

@login_required
def add_shop(request):
    gmaps = googlemaps.Client(key="AIzaSyDDv5ekhgkSI-hTpzWp8bXYwxrP0D8IBjQ")  # Replace "YOUR_API_KEY" with your actual API key
    form = CoffeeShopForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CoffeeShopForm(request.POST, request.FILES)  # Pass request.FILES to handle image upload
        if form.is_valid():
            shop = form.save(commit=False)  # Don't commit yet to set owner_id
            shop.owner_id = request.user  # Set the owner_id to the user submitting the form
            shop.save()
            
            address = (str(shop.address_line_1) + ", " + str(shop.postcode) + ", " +
                       str(shop.city) + ", " + str(shop.country))
            result = gmaps.geocode(address)
            if result:
                location = result[0].get("geometry", {}).get("location")
                if location:
                    shop.lat = location.get("lat")
                    shop.lng = location.get("lng")
                    shop.save()
                    return redirect('/BrewReview/')
                else:
                    print("Invalid address")
            else:
                print("Invalid address")
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

            # Calculate the new average rating
            new_avg_rating = Review.objects.filter(coffee_shop=shop).aggregate(Avg('rating'))['rating__avg']
            if new_avg_rating is not None:
                # Update the coffee shop rating with the new average rating
                shop.rating = round(new_avg_rating, 1)  # Round to one decimal place
                shop.save()

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
def change_username(request):
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['new_username']
            request.user.username = new_username
            request.user.save()
            return redirect('BrewReview:profile')  # Redirect to user profile page
    else:
        form = ChangeUsernameForm()
    return render(request, 'BrewReview/change_username.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
    return redirect('BrewReview:index')

@login_required
def profile(request):
    shops = []
    favourites = []
    try:
        user_id = request.user.id
        user_reviews = Review.objects.filter(user=user_id)
        recent_reviews=user_reviews.order_by('-date')
        for review in recent_reviews:
            shop_name = CoffeeShop.objects.get(pk=review.coffee_shop_id).name
            slug = CoffeeShop.objects.get(pk=review.coffee_shop_id).slug
            review.shop_name = shop_name
            review.shop_slug = slug 
            shop_info = {
                'name': review.coffee_shop.name,
                'slug': review.coffee_shop.slug,
                'rating': review.coffee_shop.rating
            }
            shops.append(shop_info)
    except:
        shops = None
        recent_reviews = None
    try:
        favourite_shops = FavouriteShops.object.filter(user=user_id)
        for favourite in favourite_shops:
            shop_name = CoffeeShop.objects.get(pk=favourite.coffee_shop_id).name
            slug = CoffeeShop.objects.get(pk=favourite.coffee_shop_id).slug
            favourite.shop_name = shop_name
            favourite.shop_slug = slug 
            shop_info = {
                'name': favourite.coffee_shop.name,
                'slug': favourite.coffee_shop.slug,
                'rating': favourite.coffee_shop.rating
            }
            favourites.append(shop_info)
    except:
        favourites = None
    return render(request, 'BrewReview/profile.html', context = {'navbar_active':'profile', 'recent_reviews': recent_reviews, 'shops':shops, 'favourites':favourites})

