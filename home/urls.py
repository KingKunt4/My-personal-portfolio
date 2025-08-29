from django.urls import path
from . import views
urlpatterns = [
    path('devices/', views.Devices, name='devices'),
    path('home/', views.welcome, name='home'),
]