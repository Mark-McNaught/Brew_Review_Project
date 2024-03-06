import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Brew_Review_Project.settings')

import django
django.setup()

import random
from django.contrib.auth.models import User
from BrewReview.models import CoffeeShop, Review, Addresses
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
        "name": "Coffee Shop F",
        "address_line_1": "1315 Oak St",
        "postcode": "54321",
        "city": "Somewhereville",
        "country": "USA",
        "description": "A trendy coffee spot with a rustic ambiance.",
        "image_location_folder": "https://example.com/image6.jpg",
        "serves_food": True,
        "rating": 4,
        "price": 3
    },
    {
        "name": "Coffee Shop G",
        "address_line_1": "1719 Cedar St",
        "postcode": "13579",
        "city": "Anytown",
        "country": "USA",
        "description": "A hip coffee joint with live music on weekends.",
        "image_location_folder": "https://example.com/image7.jpg",
        "serves_food": False,
        "rating": 5,
        "price": 4
    },
    {
        "name": "Coffee Shop H",
        "address_line_1": "2022 Walnut St",
        "postcode": "97531",
        "city": "Anothercity",
        "country": "USA",
        "description": "An upscale coffee bar serving specialty blends.",
        "image_location_folder": "https://example.com/image8.jpg",
        "serves_food": True,
        "rating": 4,
        "price": 3
    },
    {
        "name": "Coffee Shop I",
        "address_line_1": "2325 Birch St",
        "postcode": "24680",
        "city": "Yetanothercity",
        "country": "USA",
        "description": "A cozy spot offering organic coffee and vegan treats.",
        "image_location_folder": "https://example.com/image9.jpg",
        "serves_food": True,
        "rating": 4,
        "price": 2
    },
    {
        "name": "Coffee Shop J",
        "address_line_1": "2628 Pine St",
        "postcode": "86420",
        "city": "Somewhereville",
        "country": "USA",
        "description": "A hidden gem serving the best espresso in town.",
        "image_location_folder": "https://example.com/image10.jpg",
        "serves_food": False,
        "rating": 5,
        "price": 5
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
        address = Addresses.objects.create(
            address_line_1=shop_info["address_line_1"],
            postcode=shop_info["postcode"],
            city=shop_info["city"],
            country=shop_info["country"],
            lat=0.0,  # Provide latitude value here
            long=0.0   # Provide longitude value here
        )
        coffee_shop = CoffeeShop.objects.create(
            name=shop_info["name"],
            address=address,
            description=shop_info["description"],
            image_location_folder=shop_info["image_location_folder"],
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
                rating=random.randint(1, 5),
                review=random.choice(review_data)
            )
            review.save()

if __name__ == '__main__':
    print('Starting BrewReview population script...')
    populate()
