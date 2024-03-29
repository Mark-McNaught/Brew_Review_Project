from django.urls import path
from BrewReview import views


app_name = 'BrewReview'


urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),

    path('shops/', views.shops, name='shops'),
    path('shops/<slug:shop_slug>/', views.show_shop, name='show_shop'),
    path('add_shop/', views.add_shop, name='add_shop'),
    path('remove_shop/<slug:slug>', views.remove_shop, name='remove_shop'),

    path('shops/<slug:shop_slug>/add_review/', views.add_review, name='add_review'),
    path('remove_review/<int:review_id>/', views.remove_review, name='remove_review'),

    path('searched/', views.searched, name='searched'),

    path('profile/', views.profile, name='profile'),
    path('account_settings/', views.account_settings, name='account_settings'),
    path('change_username/', views.change_username, name='change_username'),
    path('delete_account/', views.delete_account, name='delete_account'),

]
