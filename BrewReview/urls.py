from django.urls import path
from BrewReview import views


app_name = 'BrewReview'


urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),

    path('shops/', views.shops, name='shops'),
    path('shops/<slug:shop_slug>/', views.show_shop, name='show_shop'),
    path('add_shop/', views.add_shop, name='add_shop'),
    path('searched/', views.searched, name='searched'),

    path('profile/', views.profile, name='profile'),
    path('account_settings/', views.account_settings, name='account_settings'),
    
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]
