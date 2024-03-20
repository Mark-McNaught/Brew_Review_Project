from django.urls import path
from BrewReview import views


app_name = 'BrewReview'


urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),

    path('shops/', views.shops, name='shops'),
    path('shops/<slug:shop_slug>/', views.show_shop, name='show_shop'),
    path('add_shop/', views.add_shop, name='add_shop'),
    path('shops/<slug:shop_slug>/add_review/', views.add_review, name='add_review'),
    path('searched/', views.searched, name='searched'),

    path('register_profile/', views.register_profile, name='register_profile'),
    path('profile/', views.profile, name='profile'),
    path('account_settings/', views.account_settings, name='account_settings'),
    path('change_username/', views.change_username, name='change_username'),

]
