from django.urls import path

from . import views

urlpatterns = [
	#dashboard/
    path('', views.dashboard, name='dashboard'),
    path('addListing/', views.addListing, name='addListing'),
    path('sell/', views.sell, name='sell'),
    path('edit/', views.edit, name='edit')
]