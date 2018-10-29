from django.urls import path

from . import views

urlpatterns = [
    # /details/...
    path('home_buyer/<int:object_id>/', views.detail, name='hbdetail'),
    path('land/<int:object_id>/', views.detail, name='detail'),
    path('project/<int:object_id>/', views.detail, name='detail'),
    path('builder/<int:object_id>/', views.detail, name='bdetail'),
    path('landlord/<int:object_id>/', views.detail, name='lldetail')
]