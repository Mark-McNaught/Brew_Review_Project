from django.contrib import admin

from BrewReview.models import CoffeeShop, Review

class CoffeeShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'rating', 'price')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('coffee_shop', 'user', 'rating', 'review')


admin.site.register(CoffeeShop, CoffeeShopAdmin)
admin.site.register(Review, ReviewAdmin)
