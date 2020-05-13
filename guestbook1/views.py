from django.http import JsonResponse
from django.shortcuts import render, redirect
from guestbook1.models import Comment, Comment_reply
from blog_v2.models import Post

from .forms import CommentForm

from django.views.decorators.csrf import csrf_exempt

def get_test(request):

    if request.method == 'POST':        
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        
        print("{}：{}".format(name, message))

        comment = Comment()
        comment.name = name
        comment.email = email
        comment.text = message
        comment.save()
        mes = '資料已儲存'
        return redirect('/guestbook1/test/')

    return render(request, 'guestbook1/test.html')        
   
@csrf_exempt
def get_ajax(request):

    if request.is_ajax():
        print('ajax_is'+request.POST.get("id"))

        id_comment = request.POST.get("id")
        id_name = request.POST.get("id_name")

        id_text = request.POST.get("id_text")

        if id_text != "" and id_name != "":
            if request.POST.get("id_email") == None:
                id_email = ""
            else:
                id_email = request.POST.get("id_email")

            com = Comment.objects.get(id=id_comment)

            try:
                Comment_reply.objects.create(name=id_name, email=id_email, text=id_text, comment=com)
            except:
                rel = "fail"
            else:
                rel = "success"
        else:
            rel = "fail"

    return JsonResponse(rel, safe=False)


# def get_commentform(request):
#     print('get_commentform')
#     if request.method == 'POST':
#
#         commentform = CommentForm(request.POST)
#         if commentform.is_valid():
#             print('a2')
#             name = commentform.cleaned_data['name']
#             email = commentform.cleaned_data['email']
#             text = commentform.cleaned_data['text']
#
#             Comment.objects.create(name = name, email = email, text = text, post = Post.objects.get(id = 4))
#
#             return redirect('/guestbook1/beta')
#
#     else:
#         get_commentform = CommentForm()
#
#
#     comment = Comment.objects.order_by('-id')
#     return render(request, 'guestbook1/forms.html', locals())

@csrf_exempt
def get_commentform(request):
    print('get_commentform')
    if request.method == 'POST':

        commentform = CommentForm(request.POST)
        print('a1')

        if request.is_ajax():
            print('ajax_is')
            id_comment = request.POST.get("id")
            id_name = request.POST.get("id_name")

            if request.POST.get("id_email") == None:
                id_email = ""
            else:
                id_email = request.POST.get("id_email")

            id_text = request.POST.get("id_text")

            rel = "{}|{}|{}".format(id, id_name, id_text)

            com = Comment.objects.get(id=id_comment)

            Comment_reply.objects.create(name=id_name, email=id_email, text=id_text, comment=com)

            return redirect('/guestbook1/beta')

        if commentform.is_valid():
            print('a2')
            name = commentform.cleaned_data['name']
            email = commentform.cleaned_data['email']
            text = commentform.cleaned_data['text']


            Comment.objects.create(name = name, email = email, text = text, post = Post.objects.get(id = 4))

            return redirect('/guestbook1/beta')

        else:
            mes = '資料驗證錯誤'

    else:
        mes = ''
        commentform = CommentForm()


    get_commentform = CommentForm()
    comment = Comment.objects.order_by('-id')
    return render(request, 'guestbook1/forms.html', locals())

def get_comment(request):
    print('get_comment')
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        print("{}：{}".format(name, message))

        comment = Comment()
        comment.name = name
        comment.email = email
        comment.text = message
        comment.save()

        return redirect('/guestbook1/')

    comment = Comment.objects.order_by('-id')
    return render(request, 'guestbook1/guestbook.html', locals())

    
    
    