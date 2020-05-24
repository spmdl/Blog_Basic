from django.contrib import admin
from django.urls import path, include, re_path
from . import views

from django.views.static import serve
from Blog_Basic.settings import MEDIA_ROOT

urlpatterns = [
    # path('', views.sign, name='sign'),
    path('up/', views.signup, name='signup'),
    path('in/', views.signin, name='signin'),
    path('out/', views.signout, name='signout'),

]
