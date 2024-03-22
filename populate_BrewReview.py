import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Brew_Review_Project.settings')

import django
django.setup()

import random
from django.contrib.auth.models import User
from BrewReview.models import CoffeeShop, Review
from datetime import datetime, timedelta


def populate():
    # Sample data for CoffeeShops
    coffee_shop_data = [
        {
            "name": "Andina Colombian Cafe",
            "address_line_1": "1274 Argyle St",
            "postcode": "G3 8AA",
            "city": "Glasgow",
            "country": "UK",
            "lat":55.86654919999999,
            "lng":-4.2895653,
            "description": "A trendy coffee spot with a rustic ambiance.",
            "serves_food": True,
            "rating": 3,
            "price": 4
        },
        {
            "name": "West End Coffee House & Bakery",
            "address_line_1": "683 Great Western Rd",
            "postcode": "G12 8RA",
            "city": "Glasgow",
            "country": "UK",
            "lat": 55.8770116,
            "lng": -4.287652899999999,
            "description":"Indulge in the essence of leisure and sophistication at our chic coffee haven nestled in Glasgow's vibrant West End.",
            "serves_food": True,
            "rating": 4,
            "price": 3
        },
        {
            "name": "Tinderbox",
            "address_line_1": "189 Byres Rd",
            "postcode": "G12 8TS",
            "city": "Glasgow",
            "country": "UK",
            "lat": 55.8739949,
            "lng": -4.2953535,
            "description":"Experience the epitome of artisanal coffee culture amidst the eclectic charm of Glasgow's West End at our cozy café retreat.",
            "serves_food": False,
            "rating": 5,
            "price": 5
        },
        {
            "name": "Grain and Grind",
            "address_line_1": "45 Old Dumbarton Rd",
            "postcode": "G3 8RF",
            "city": "Glasgow",
            "country": "UK",
            "lat": 55.867053,
            "lng": -4.292545,
            "description":"Embrace Glasgow's coffee culture at our inviting café, where every cup tells a story of community and craftsmanship.",
            "serves_food": False,
            "rating": 2,
            "price": 4
        },
        {
            "name": "University Cafe",
            "address_line_1": "87 Byres Rd",
            "postcode": "G11 5HN",
            "city": "Glasgow",
            "country": "UK",
            "lat": 55.872035,
            "lng": -4.297690999999999,
            "description":"Sip on handcrafted perfection in the heart of Glasgow's West End at our cozy coffee sanctuary.",
            "serves_food": True,
            "rating": 2,
            "price": 2
        },
        {
            "name": "Caffe Nero",
            "address_line_1": "78 Queen St",
            "postcode": "G1 3DN",
            "city":"Glasgow",
            "country": "UK",
            "lat": 55.85967851333062,
            "lng": -4.242060419352726,
            "description":"Casual coffee shop with a menu of light dishes & specially blended hot & cold drinks.",
            "serves_food": True,
            "rating": 4,
            "price": 2
        },
        {
           "name":"Laboratorio Espresso",
            "address_line_1":"93 W Nile St",
            "postcode": "G1 2SH",
            "city":"Glasgow",
            "country": "UK",
            "lat": 55.86331810783141,
            "lng": -4.253763321841493,
            "description":"Small, relaxed outpost serving coffee drinks, sandwiches, hot specials, pastries & baked goods.",
            "serves_food": True,
            "rating": 3,
            "price":3
        },
        {
            "name":"Riverhill Coffee Bar",
            "address_line_1":"24 Gordon St",
            "postcode":"G1 3PU",
            "city":"Glasgow",
            "country":"UK",
            "lat":55.86068591639749,
            "lng":-4.254934696706068,
            "description":"Low-key cafe with bar seating serving sandwiches, hot specials and homemade cakes and pastries.",
            "serves_food": True,
            "rating": 2,
            "price": 1,

        },
        {
            "name":"Spill The Beans",
            "address_line_1": "19 Skirving St",
            "postcode": "G41 3AB",
            "city":"Glasgow",
            "country": "UK",
            "lat":55.82858651853124,
            "lng": -4.280189304108775,
            "description":"Laid-back chain serving artisan coffee, light snacks and pastries in a comfy space with music.",
            "serves_food": False,
            "rating": 4,
            "price":3
        },
        {
            "name":"Common Ground",
            "address_line_1": "186 Battlefield Rd",
            "postcode": "G42 9JT",
            "city":"Glasgow",
            "country":"UK",
            "lat":55.825771144324605,
            "lng":-4.264334125002118,
            "description":"Best coffee in the South Side",
            "serves_food": False,
            "rating":5,
            "price":3
        },
        {
            "name":"Short Long Black",
            "address_line_1": "501 Victoria Rd",
            "postcode": "G42 8RL",
            "city":"Glasgow",
            "country":"UK",
            "lat":55.835250225468435,
            "lng":-4.263235502574541,
            "description":"Perk up your day at Short Long Black, where expertly crafted coffee meets cozy ambiance and community spirit.",
            "serves_food": False,
            "rating":3,
            "price":2
        },
        {
            "name":"The Brooklyn Cafe",
            "address_line_1": " Minard Rd",
            "postcode": "G41 2HR",
            "city":"Glasgow",
            "country":"UK",
            "lat":55.831980686499755,
            "lng": -4.279127732944331,
            "description":"Modern coffee shop",
            "serves_food": True,
            "rating":5,
            "price":3
        },
        {
            "name":"Daily Coffee",
            "address_line_1": "160 Garthland Dr",
            "postcode": "G31 2SP",
            "city":"Glasgow",
            "country":"UK",
            "lat":55.860382880882376,
            "lng": -4.214243280820654,
            "description":"Discover the heart and soul of Glasgow's East End through the rich aroma and warm embrace of our locally loved coffee shop.",
            "serves_food": False,
            "rating":2,
            "price":4
        },
        {
            "name":"Zennor",
            "address_line_1": "354 Duke St",
            "postcode": "G31 1RB",
            "city":"Glasgow",
            "country":"UK",
            "lat":55.85868776353587,
            "lng":-4.218209233078885,
            "description":"Savor the vibrant flavors of artisanal coffee amidst the eclectic charm of Glasgow's East End at our welcoming neighborhood café.",
            "serves_food": True,
            "rating": 4,
            "price": 4

        }
    ]

    titles = [
        "Great",
        "Poor",
        "Ok",
        "Nice",
        "Decent"
    ]

    # Sample data for Reviews
    review_data = [
        "Great coffee and atmosphere!",
        "The service was excellent.",
        "Average coffee, but the pastries were delicious.",
        "Nice place to hang out with friends.",
        "Not impressed with the quality of coffee."
    ]

    review_users = []
    usernames = ["Sophia Rodriguez","Benjamin Thompson","Emily Patel",
                 "Joshua Nguyen","Isabella Williams"]
    for i in range(5):
        username = usernames[i]
        user = User.objects.create(username=username)
        user.set_password('password')
        user.save()
        review_users.append(user)

    # Create CoffeeShops
    for shop_info in coffee_shop_data:
        owner_username = f"{shop_info['name'].replace(' ', '')}_owner"
        owner = User.objects.create(username=owner_username)
        owner.set_password('password')
        owner.save()

        coffee_shop = CoffeeShop.objects.create(
            name=shop_info["name"],
            owner_id=owner,
            address_line_1=shop_info["address_line_1"],
            postcode=shop_info["postcode"],
            city=shop_info["city"],
            country=shop_info["country"],
            lat=shop_info["lat"],
            lng=shop_info["lng"],
            description=shop_info["description"],
            serves_food=shop_info["serves_food"],
            rating=shop_info["rating"],
            price=shop_info["price"]
        )

        for user in review_users:
            review = Review.objects.create(
                coffee_shop=coffee_shop,
                user=user,
                date=datetime.now() - timedelta(days=random.randint(1, 365)),
                title=random.choice(titles),
                rating=random.randint(1, 5),
                review=random.choice(review_data)
            )
            review.save()

if __name__ == '__main__':
    print('Starting BrewReview population script...')
    populate()
