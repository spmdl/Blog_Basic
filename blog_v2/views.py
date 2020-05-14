from django.shortcuts import render, redirect
from blog_v2.models import Post, Catalog, Navbar
from guestbook1.models import Comment,Comment_reply



from django.urls import NoReverseMatch, reverse

from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .forms import CommentForm

import math


from django.views.decorators.csrf import csrf_exempt

from django.db.models import Q


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


def post_search(request):
    print('post_search')

    print(request.POST["search"])


    if 'search' in request.POST and request.POST["search"] != '':
        get_search = request.POST.get("search")
    else:
        message = 'You submitted an empty form.'



    blog = Post.objects.filter(Q(title__icontains=get_search) | Q(content__icontains=get_search)).order_by('-id')
    work = Post.objects.last()
    catalog = Navbar.objects.all()
    catalog_tag = Catalog.objects.all()


    return render(request, 'blog_v2/index_blog.html', locals())
    # return redirect('index')

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



@csrf_exempt
def post_ajax(request, post_id):
    print("ajax")

    if request.is_ajax():
        # print('ajax_is'+request.POST.get("id"))

        id_comment = request.POST.get("id")
        id_name = request.POST.get("id_name")
        id_text = request.POST.get("id_text")
        but_name = request.POST.get("but_name")
        post_id = post_id

        if id_text != "" and id_name != "":
            if request.POST.get("id_email") == "":
                id_email = ""
            else:
                id_email = request.POST.get("id_email")

            if but_name == 'reply':
                com = Comment.objects.get(id=id_comment)
                try:
                    new_com = Comment_reply.objects.create(name=id_name, email=id_email, text=id_text, comment=com)
                except:
                    rel = "fail"
                else:
                    rel = "success"
                daytime = new_com.create_time
                timeArray = "{}.{:0>2d}.{:0>2d}".format(daytime.year, daytime.month, daytime.day)
                return JsonResponse({
                    'rel': rel,
                    'id': new_com.id,
                    'text': id_text,
                    'name': id_name,
                    'create_time': timeArray,
                    'button':but_name,
                    'class_name':"reply" + id_comment
                }, safe=False)

            else:
                post = Post.objects.get(id=post_id)
                counter = post.post_comment.count()

                try:
                    new_com = Comment.objects.create(name=id_name, email=id_email, text=id_text, post=post)
                except:
                    rel = "fail"
                else:
                    rel = "success"
                daytime = new_com.create_time
                timeArray = "{}.{:0>2d}.{:0>2d}".format(daytime.year, daytime.month, daytime.day)
                return JsonResponse({
                    'rel': rel,
                    'id': new_com.id,
                    'text': id_text,
                    'name': id_name,
                    'create_time': timeArray,
                    'button': but_name,
                }, safe=False)


        else:
            rel = "fail"
    else: rel = "fail"

    return JsonResponse({'rel':rel}, safe=False)






def post_beta(request, post_id):
    
    blog = Post.objects.all().filter(id = post_id)
    work = Post.objects.last()
    catalog = Navbar.objects.all()
    catalog_tag = Catalog.objects.all()
    comments = Post.objects.get(id = post_id).post_comment.all()
    get_commentform = CommentForm()
    post_id = post_id
    
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
                    Comment.objects.create(name = name, email = email, text = text, post = post)
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
