from django.shortcuts import render, redirect
from guestbook.models import Comment

from .forms import CommentForm

def get_test(request):
    return render(request, 'guestbook/test.html')        
   
    
def get_commentform(request):

    print('get_commentform')
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            name = commentform.cleaned_data['name']
            email = commentform.cleaned_data['email']
            text = commentform.cleaned_data['text']
            com = Comment.objects.create(name = name, email = email, text = text)
            com.save()
            return redirect('/guestbook/f')
        else:
            mes = '資料驗證錯誤'
    else:
        mes = ''
        commentform = CommentForm()
        
    get_commentform = CommentForm() 
    comment = Comment.objects.order_by('-id')
    return render(request, 'guestbook/forms.html', locals())

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
        return redirect('/guestbook/')
    else:
        mes = '請輸入資料'
    print('mes:' + mes)
    comment = Comment.objects.order_by('-id')
    return render(request, 'guestbook/guestbook.html', locals())
    
    
    
    