from django.contrib import admin

from BrewReview.models import CoffeeShop, Review

class CoffeeShopAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'address_line_1','postcode','city','country', 'rating', 'price')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('coffee_shop', 'user', 'rating', 'review', 'date')



admin.site.register(CoffeeShop, CoffeeShopAdmin)
admin.site.register(Review, ReviewAdmin)
