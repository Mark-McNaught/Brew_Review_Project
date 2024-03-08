from typing import Any
from django import forms
from django.contrib.auth.models import User
from BrewReview.models import UserProfile


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