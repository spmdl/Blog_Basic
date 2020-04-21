from django.contrib import admin
from blog_v2.models import Post, Navbar, Catalog

class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title') 
    
admin.site.register([Post, Navbar, Catalog])
admin.site.unregister(Post)
admin.site.register(Post, PostAdmin)