from django.urls import path

from . import views

from login import views as login_views

urlpatterns = [
    # /details/...
    path('home_buyer/', views.home_buyer, name='signup_home_buyer'),
    path('login/', login_views.login, name='login_landlord'),
    path('login/', login_views.login, name='login_home_buyer'),
    path('login/', login_views.login, name='login_builder'),
    path('builder/', views.builder, name='signup_builder'),
    path('landlord/', views.landlord, name='signup_landlord')
]