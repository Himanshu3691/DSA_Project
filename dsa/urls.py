from django.urls import path
from .views import * 

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path('about/vali/', vali, name='vali'),
    path('user_pro/<int:id>/', UserPro.as_view(), name='user_pro'),
    path('code/<int:id>', Code.as_view(), name='code'),
    path('register/', register, name='register'),


]
