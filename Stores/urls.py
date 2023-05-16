from django.urls import path, include
from . import views

urlpatterns = [
    path("home", views.index, name='Home'),
    path("loging", views.loging, name='loging'),
    path("signup", views.signup, name='signup'),
]