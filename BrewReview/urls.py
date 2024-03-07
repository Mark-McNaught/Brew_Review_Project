from django.urls import path
from BrewReview import views


app_name = 'BrewReview'


urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('profile/', views.profile, name='profile'),
    path('usersettings/', views.user_settings, name='user_settings'),
    path('shops/', views.shops, name='shops'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]
