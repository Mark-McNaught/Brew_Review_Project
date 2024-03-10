from typing import Any
from django import forms
from django.contrib.auth.models import User
from BrewReview.models import UserProfile, CoffeeShop, Review
import googlemaps


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','password',)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password != confirm:
            raise forms.ValidationError(
                "Passwords must match"
            )


class UserProfileForm(forms.ModelForm):
    owner = forms.BooleanField(required=False)
    
    class Meta:
        model = UserProfile
        fields = ()



class CoffeeShopForm(forms.ModelForm):
    gmaps = googlemaps.Client(key="AIzaSyDDv5ekhgkSI-hTpzWp8bXYwxrP0D8IBjQ")
    name = forms.CharField(max_length=CoffeeShop.NAME_MAX_LENGTH, help_text="Please enter the shop name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    address_line_1 = forms.CharField(max_length=128, help_text="Please enter the first line of address")
    postcode = forms.CharField(max_length=128, help_text="Please enter the postcode")
    city = forms.CharField(max_length=128, help_text="Please enter the city")
    country = forms.CharField(max_length=128, help_text="Please enter the country")
    # result = (gmaps.geocode(str(address_line_1) + ", " + str(postcode) + ", " +
    #                         str(city) + ", " + str(country))[0]
    #           .get("geometry", None).get("location", None))
    # if result:
    #     lat = result.get("lat")
    #     lng = result.get("lng")
    #else:
        #invalid addresss
    description = forms.CharField(max_length=CoffeeShop.DESC_MAX_LENGTH, help_text="Please enter a shop description.")
    image_location_folder = "Not sure yet"
    serves_food = forms.BooleanField(help_text="Please enter if the shop serves food.", required=False)
    rating = "Not sure yet"
    price = forms.IntegerField(help_text="Please enter how expensive the shop is on a range 1 to 5.", max_value=5)

    # class Meta:
    #     model = Addresses
    #     fields = ('address_line_1', 'postcode', 'city', 'country', )
    class Meta:
        model = CoffeeShop
        fields = ('name','description','serves_food','price','address')


class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=Review.TITLE_MAX_LENGTH, help_text="Please enter the title of the review.")
    rating = forms.IntegerField(help_text="Please enter your rating of the shop on a range 1 to 5.", max_value=5)
    review = forms.CharField(max_length=Review.REVIEW_MAX_LENGTH, help_text="Please enter your review of the shop.")


    class Meta:
        model = Review
        fields = ('title', 'rating', 'review')




    