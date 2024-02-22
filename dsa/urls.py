from django.urls import path
from . import views
from dsa import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path('home/', views.home, name='home'),
    path('about/vali/', views.vali, name='vali'),

]