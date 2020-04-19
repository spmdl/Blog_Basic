from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'index.html')

def blog(request):
    blog = Post.objects.all()
    
    return render(request, 'index_blog.html', {
        'blog': blog, 
    })

def index(request):
    blog = Post.objects.all()
    
    return render(request, 'blog.html', {
        'blog': blog, 
    })