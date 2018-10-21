from django.urls import path

from . import views

urlpatterns = [
    # /details/...
    path('landlord/', views.login_landlord, name='login_landlord'),
    path('builder/', views.login_builder, name='login_builder'),
    path('home_buyer/', views.login_home_buyer, name='login_home_buyer')
]