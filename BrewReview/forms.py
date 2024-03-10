from typing import Any
from django import forms
from django.contrib.auth.models import User
from BrewReview.models import UserProfile, CoffeeShop, Review


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
    owner = forms.BooleanField()
    
    class Meta:
        model = UserProfile
        fields = ()



class CoffeeShopForm(forms.ModelForm):
    name = forms.CharField(max_length=CoffeeShop.NAME_MAX_LENGTH, help_text="Please enter the shop name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    address = "not sure what to do here yet"
    description = forms.CharField(max_length=CoffeeShop.DESC_MAX_LENGTH, help_text="Please enter a shop description.")
    image_location_folder = "Not sure yet"
    serves_food = forms.BooleanField(help_text="Please enter if the shop serves food.")
    rating = "Not sure yet"
    price = forms.IntegerField(help_text="Please enter how expensive the shop is on a range 1 to 5.")
    
    class Meta:
        model = CoffeeShop
        fields = ('name','description','serves_food','price')


class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=Review.TITLE_MAX_LENGTH, help_text="Please enter the title of the review.")
    rating = forms.IntegerField(help_text="Please enter your rating of the shop on a range 1 to 5.")
    review = forms.CharField(max_length=Review.REVIEW_MAX_LENGTH, help_text="Please enter your review of the shop.")


    class Meta:
        model = Review
        fields = ('title', 'rating', 'review')




    