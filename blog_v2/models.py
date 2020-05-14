from django.db import models
from datetime import date

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(default=date.today)
    tag = models.CharField(max_length=15)
#     src = models.FilePathField(upload_to='media/')
    src = models.FileField(default = None)
    
    class Meta:
        app_label='blog_v2'
    
    def __str__(self):
        return ("{}".format(self.title))
    
class Navbar(models.Model):
    catalog = models.CharField(max_length=15)
    
    class Meta:
        app_label='blog_v2'    
    
    def __str__(self):
        return ("{}".format(self.catalog))
    
class Catalog(models.Model):
    tag = models.CharField(max_length=15)

    class Meta:
        app_label='blog_v2'    
    def __str__(self):
        return ("{}".format(self.tag))
    
# class PostAdmin(admin.ModelAdmin):
# 	list_display = ('id', 'title') 

    