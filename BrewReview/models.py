from django.db import models
from django.contrib.auth.models import User

class CoffeeShop(models.Model):
    # Table for storing details about a coffee shop
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256, unique=True)
    description = models.TextField(max_length=1000)
    image_location_folder = models.URLField(max_length=256, unique=True)
    serves_food = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Review(models.Model):
    # Table for storing details about a coffee shop review
    coffee_shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    rating = models.IntegerField(default=0)
    review = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.id)



"""
# will implement once main site is working

class UserContent(models.Model):
    # Table for storing a users favourite restaurants and saved reviews
    # Need to double check foreignKey is correct
    
    user = OneToOneField(User, on_delete=models.CASCADE)
    fav1 = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    fav2 = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    fav3= models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    save1 = models.ForeignKey(Review, on_delete=models.CASCADE)
    save2 = models.ForeignKey(Review, on_delete=models.CASCADE)
    save3 = models.ForeignKey(Review, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
"""