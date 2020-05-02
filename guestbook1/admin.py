from django.contrib import admin
from guestbook1.models import Comment, Comment_reply

admin.site.register([Comment, Comment_reply])