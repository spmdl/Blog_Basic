from django.urls import path
from . import views
from Blog_Basic.settings import MEDIA_ROOT

urlpatterns = [
    path('', views.get_comment),
    path('beta/', views.get_commentform),
    path('ajax/', views.get_ajax),
#     re_path('media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
#     path('gu/', views.index),
    path('test/', views.get_test),

]
