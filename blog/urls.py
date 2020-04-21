from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.index),
    path('home', views.home, name='blog'),
    path('blog', views.blog, name='blog'),
    path('index', views.blog, name='blog'),
]
