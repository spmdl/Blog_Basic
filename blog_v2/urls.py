from django.contrib import admin
from django.urls import path, include, re_path
from . import views

from django.views.static import serve
from Blog_Basic.settings import MEDIA_ROOT

urlpatterns = [
    path('', views.index),
    re_path('media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})

]
