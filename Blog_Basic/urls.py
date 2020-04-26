from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('blog_v2.urls')),
    path('blog_v2/', include('blog_v2.urls')),
    path('guestbook/', include('guestbook.urls')),
]
