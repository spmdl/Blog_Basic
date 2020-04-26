from django.shortcuts import render, redirect
from blog_v2.models import Post, Catalog, Navbar


from django.http import HttpResponseRedirect


import math

def index(request):
    print('index')    
    blog = Post.objects.order_by('-id')
    work = Post.objects.last()
    catalog = Navbar.objects.all()
    catalog_tag = Catalog.objects.all()
    return render(request, 'blog_v2/index_blog.html', locals())

def post_tag(request, post_id, get_from):
    print('post_tag')
    if get_from == 'post':
        tag_id = Post.objects.get( id = post_id)

    elif get_from == 'tag':
        tag_id = Catalog.objects.get(id = post_id)

    blog = Post.objects.filter(tag = tag_id.tag).order_by('-id')
    work = Post.objects.last()
    catalog = Navbar.objects.all()
    catalog_tag = Catalog.objects.all()
#     return redirect('index', request)
#     return HttpResponseRedirect('index')

    return render(request, 'blog_v2/index_blog.html', locals())    
        
def catalog_tag(request, catalog_id):
    print('catalog_tag')
    tag_id = Catalog.objects.get(id = catalog_id)
    blog = Post.objects.filter(tag = tag_id.tag).order_by('-id')
    work = Post.objects.last()
    catalog = Navbar.objects.all()
    catalog_tag = Catalog.objects.all()
    return render(request, 'blog_v2/index_blog.html', locals())

def post_test(request, post_id):
    blog = Post.objects.all().filter(id = post_id)
    work = Post.objects.last()
    catalog = Navbar.objects.all()
    catalog_tag = Catalog.objects.all()
    return render(request, 'blog_v2/post.html', locals())

def post(request):
    blog = Post.objects.all()
    work = Post.objects.last()
    catalog = Navbar.objects.all()
    catalog_tag = Catalog.objects.all()
    return render(request, 'blog_v2/index_post.html', {
        'blog': blog, 
        'work': work,
        'catalog':catalog,
        'catalog_tag': catalog_tag,
    })

def guestbook(request):
    blog = Post.objects.all()
    work = Post.objects.last()
    return render(request, 'blog_v2/gu.html', {
        'blog': blog, 
        'work': work,
    })
