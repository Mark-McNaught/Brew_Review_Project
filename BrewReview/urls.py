from django.urls import path
from BrewReview import views


app_name = 'BrewReview'


urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('shops/', views.shops, name='shops'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]
