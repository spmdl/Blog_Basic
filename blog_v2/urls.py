from django.contrib import admin
from django.urls import path, include, re_path
from . import views

from django.views.static import serve
from Blog_Basic.settings import MEDIA_ROOT

urlpatterns = [
    path('', views.index, name='index'),
#     path('post/', views.post),
    path('tag/<int:post_id>/<str:get_from>', views.post_tag, name='post_tag'),
    path('post/<int:post_id>/', views.post_test, name='post'),
    path('post_beta/<int:post_id>/<int:postgu_id>/', views.post_beta, name='postgu_beta'),
    
    path('post_beta/<int:post_id>/', views.post_beta, name='post_beta'),
    path('post_ajax/<int:post_id>', views.post_ajax, name='post_ajax'),

#     path('gu', views.guestbook),
    re_path('media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]
