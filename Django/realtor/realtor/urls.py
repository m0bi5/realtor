from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('details/', include('details.urls')),
    path('search/', include('search.urls')),
    path('signup/', include('signup.urls')),
    path('login/', include('login.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
]