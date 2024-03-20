from typing import Any
from django import forms
from django.contrib.auth.models import User
from BrewReview.models import UserProfile, CoffeeShop, Review
import googlemaps


class UserProfileForm(forms.ModelForm):
    owner = forms.BooleanField(required=False)
    picture = forms.ImageField(required=False)
    
    class Meta:
        model = UserProfile
        fields = ('picture', 'owner')



class CoffeeShopForm(forms.ModelForm):
    gmaps = googlemaps.Client(key="AIzaSyDDv5ekhgkSI-hTpzWp8bXYwxrP0D8IBjQ")

    name = forms.CharField(max_length=128, help_text="Please enter the shop name.")
    description = forms.CharField(max_length=1000, help_text="Please enter a shop description.")
    serves_food = forms.BooleanField(help_text="Please enter if the shop serves food.", required=False)
    price = forms.ChoiceField(widget=forms.RadioSelect, choices=[(i, i) for i in range(1, 6)], help_text="Please enter how expensive the shop is on a range 1 to 5.")
    address_line_1 = forms.CharField(max_length=128, help_text="Please enter the first line of address")
    postcode = forms.CharField(max_length=10, help_text="Please enter the postcode")
    city = forms.CharField(max_length=128, help_text="Please enter the city")
    country = forms.CharField(max_length=128, help_text="Please enter the country")

    class Meta:
        model = CoffeeShop
        fields = ('name', 'description', 'serves_food', 'price', 'address_line_1', 'postcode', 'city', 'country')


class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=Review.TITLE_MAX_LENGTH, help_text="Please enter the title of the review.")
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=[(i, i) for i in range(1, 6)], help_text="Please enter your rating of the shop on a range 1 to 5.")
    review = forms.CharField(max_length=Review.REVIEW_MAX_LENGTH, help_text="Please enter your review of the shop.")


    class Meta:
        model = Review
        fields = ('title', 'rating', 'review')


class ChangeUsernameForm(forms.Form):
    new_username = forms.CharField(max_length=150)

    