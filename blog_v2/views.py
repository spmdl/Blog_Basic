from django.shortcuts import render, redirect
from blog_v2.models import Post, Catalog, Navbar
from guestbook1.models import Comment,Comment_reply

from django.http import HttpResponseRedirect, JsonResponse
from .forms import CommentForm

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


def check_views(request):
    print('aa')



def post_beta(request, post_id):
    
    blog = Post.objects.all().filter(id = post_id)
    work = Post.objects.last()
    catalog = Navbar.objects.all()
    catalog_tag = Catalog.objects.all()
    comments = Post.objects.get(id = post_id).post_comment.all()
    get_commentform = CommentForm()
    
    print(request.POST.get("id_text"))

    if request.is_ajax():
        print('a')
    
    if request.method == 'POST':
        
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            name = commentform.cleaned_data['name']
            email = commentform.cleaned_data['email']
            text = commentform.cleaned_data['text']
            print(request.POST.get('content'))

            if 'send' in request.POST:
                if text:
                    post = Post.objects.get(id = post_id)
                    print(post)
#                     Comment.objects.create(name = name, email = email, text = text, post = post)
                return render(request, 'blog_v2/post_beta.html', locals())
            else:
                pass
       
    

    return render(request, 'blog_v2/post_beta.html', locals())

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
