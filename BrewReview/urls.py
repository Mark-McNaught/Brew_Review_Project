from django.urls import path
from BrewReview import views


app_name = 'BrewReview'


urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('profile/', views.profile, name='profile'),
    path('shops/', views.shops, name='shops'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('account_settings/', views.account_settings, name='account_settings'),
    path('logout/', views.user_logout, name='logout'),
]
