from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return ("標題:{}, 字數:{}, 摘要:{}".format(self.title, len(self.content), self.content[:10]))
