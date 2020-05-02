from django.db import models
from datetime import date
from django.utils import timezone
from blog_v2.models import Post

class Comment(models.Model):
    name = models.CharField(max_length=15, null=False, blank=False, default="Visitors")
    email = models.EmailField(null=False, blank=True, default="")
    text = models.TextField()
    create_time = models.DateTimeField( default=timezone.now, null=False, blank=False)                   
    post = models.ForeignKey('blog_v2.Post', on_delete=models.CASCADE, related_name="post_comment")

    class Meta:
        ordering = ['-create_time']
        db_table = "Comment_1"
                            
    def __str__(self):
            return '{}'.format(self.text)

class Comment_reply(models.Model):    
    name = models.CharField(max_length=15, null=False, blank=False, default="Visitors")
    email = models.EmailField(null=False, blank=True, default="")
    text = models.TextField()
    create_time = models.DateTimeField( default=timezone.now, null=False, blank=False)
    comment = models.ForeignKey('guestbook1.Comment', on_delete=models.CASCADE, related_name="comment_reply")
    
    class Meta:
        ordering = ['-create_time']
        db_table = "Comment_reply_1"
                            
    def __str__(self):
            return '{}'.format(self.text)
    
    
    
    
    