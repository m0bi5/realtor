from django.urls import path

from . import views

urlpatterns = [
	#dashboard/
    path('', views.dashboard, name='dashboard'),
    path('edit/', views.edit, name='edit')
]