from django.contrib import admin

from BrewReview.models import CoffeeShop, Review, SavedReviews, FavouriteShops, UserProfile

class CoffeeShopAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'address', 'rating', 'price')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('coffee_shop', 'user', 'rating', 'review')

class SavedReviewsAdmin(admin.ModelAdmin):
    list_display = ('save_id', 'review_id', 'user')

class FavouriteShopsAdmin(admin.ModelAdmin):
    list_display = ('fav_id', 'shop_id', 'user')




admin.site.register(CoffeeShop, CoffeeShopAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(SavedReviews)
admin.site.register(FavouriteShops)
#admin.site.register(Addresses)



admin.site.register(UserProfile)