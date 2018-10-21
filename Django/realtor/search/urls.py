from django.urls import path

from . import views

urlpatterns = [
    # /search/...
    path('', views.search, name='search')
]