from django.shortcuts import render
from blog_v2.models import Post

def index(request):
    blog = Post.objects.all()
    work = Post.objects.last()
    print(work)
    return render(request, 'blog_v2/index_blog.html', {
        'blog': blog, 
        'work': work,
    })