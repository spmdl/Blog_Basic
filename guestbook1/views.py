from django.shortcuts import render, redirect
from guestbook1.models import Comment, Comment_reply
from blog_v2.models import Post

from .forms import CommentForm

def get_test(request):

    if request.method == 'POST':        
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        
        print("{}：{}".format(name, message))
        
        o_message = Comment()
        o_message.name = name
        o_message.email = email
        o_message.text = message
        o_message.save()
        mes = '資料已儲存'
        return redirect('/guestbook1/test/')

    return render(request, 'guestbook1/test.html')        
   
    
def get_commentform(request):
    print('get_commentform')
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        num_visits = request.session.get('num_visits', 0)

        if commentform.is_valid():
            name = commentform.cleaned_data['name']
            email = commentform.cleaned_data['email']
            text = commentform.cleaned_data['text']
            
            if 'reply' in request.POST:
#                 多一個 comment 欄位
                print("reply：" + request.POST['id_comment0'])
#                 Comment.objects.get(id=)
                print(request.POST.get('text', '') + "|" + request.POST.get('comment_id', ''))
                com_rep = Comment_reply()
#                 comment = request.POST['comment']
#                 comment = request.POST.get['comment', False]

#                 comment_id = request.POST.get('comment_id', '')
#                 print(comment_id)
#                 com = Comment.objects.get(id=)
    
#                 Comment_reply.objects.create(name = name, email = email, text = text, comment=com)
            else:
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
        
        o_message = Comment()
        o_message.name = name
        o_message.email = email
        o_message.text = message
        o_message.save()
        mes = '資料已儲存'
        return redirect('/guestbook1/')
    mes = '請輸入資料'
    comment = Comment.objects.order_by('-id')
    return render(request, 'guestbook1/guestbook.html', locals())
    
    
    
    