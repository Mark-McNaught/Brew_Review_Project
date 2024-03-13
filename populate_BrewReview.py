import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Brew_Review_Project.settings')

import django
django.setup()

import random
from django.contrib.auth.models import User
from BrewReview.models import CoffeeShop, Review
from datetime import datetime, timedelta


"""
def populate():
            # Sample data for CoffeeShops
        coffee_shop_data = [
            {
                "name": "Coffee Shop A",
                "address": "123 Main St, Anytown, USA",
                "description": "A cozy cafe serving delicious coffee and pastries.",
                "image_location_folder": "https://example.com/image1.jpg",
                "serves_food": True,
                "rating": 4,
                "price": 2
            },
            {
                "name": "Coffee Shop B",
                "address": "456 Elm St, Anothercity, USA",
                "description": "A modern coffee house with a variety of coffee blends.",
                "image_location_folder": "https://example.com/image2.jpg",
                "serves_food": False,
                "rating": 5,
                "price": 3
            },
            {
                "name": "Coffee Shop C",
                "address": "789 Oak St, Yetanothercity, USA",
                "description": "An artisanal coffee shop with ethically sourced beans.",
                "image_location_folder": "https://example.com/image3.jpg",
                "serves_food": True,
                "rating": 4,
                "price": 3
            },
            {
                "name": "Coffee Shop D",
                "address": "1011 Pine St, Somewhereville, USA",
                "description": "A hipster coffee spot with a minimalist vibe.",
                "image_location_folder": "https://example.com/image4.jpg",
                "serves_food": False,
                "rating": 3,
                "price": 2
            },
            {
                "name": "Coffee Shop E",
                "address": "1213 Maple St, Anytown, USA",
                "description": "A family-owned coffee shop famous for its homemade pastries.",
                "image_location_folder": "https://example.com/image5.jpg",
                "serves_food": True,
                "rating": 5,
                "price": 4
            }
        ]

        # Sample data for Reviews
        review_data = [
            "Great coffee and atmosphere!",
            "The service was excellent.",
            "Average coffee, but the pastries were delicious.",
            "Nice place to hang out with friends.",
            "Not impressed with the quality of coffee."
        ]

        # Create CoffeeShops
        coffee_shops = []
        for shop_info in coffee_shop_data:
            coffee_shop = CoffeeShop.objects.create(**shop_info)
            coffee_shops.append(coffee_shop)

        # Create Users and Reviews
        for i in range(5):
            user = User.objects.create(username=f"User{i + 1}")
            user.set_password('password')
            user.save()

            for coffee_shop in coffee_shops:
                review = Review.objects.create(
                    coffee_shop=coffee_shop,
                    user=user,
                    date=datetime.now() - timedelta(days=random.randint(1, 365)),
                    rating=random.randint(1, 5),
                    review=random.choice(review_data)
                )
                review.save()
    
if __name__ == '__main__':
    print('Starting BrewReview population script...')
    populate()


"""

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
        "description": "A trendy coffee spot with a rustic ambiance.",
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
        "description": "A trendy coffee spot with a rustic ambiance.",
        "serves_food": True,
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
        "description": "A trendy coffee spot with a rustic ambiance.",
        "serves_food": True,
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
        "description": "A trendy coffee spot with a rustic ambiance.",
        "serves_food": True,
        "rating": 2,
        "price": 2
    },
    
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

    # Create CoffeeShops
    coffee_shops = []
    for shop_info in coffee_shop_data:
    #     address = Addresses.objects.create(
    #         address_line_1=shop_info["address_line_1"],
    #         postcode=shop_info["postcode"],
    #         city=shop_info["city"],
    #         country=shop_info["country"],
    #
    #     )

        coffee_shop = CoffeeShop.objects.create(
                name=shop_info["name"],
                address_line_1=shop_info["address_line_1"],
                postcode = shop_info["postcode"],
                city = shop_info["city"],
                country = shop_info["country"],
                lat = shop_info["lat"],
                lng = shop_info["lng"],
                description=shop_info["description"],
                serves_food=shop_info["serves_food"],
                rating=shop_info["rating"],
                price=shop_info["price"]
            )
        coffee_shops.append(coffee_shop)

    # Create Users and Reviews
    for i in range(5):
        user = User.objects.create(username=f"User{i + 1}")
        user.set_password('password')
        user.save()

        for coffee_shop in coffee_shops:
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
