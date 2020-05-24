from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages

def signin(request):

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/', locals())
        else:
            redirect('/signin', locals())
    else:
        return render(request, 'signup/signin.html', locals())

def signup(request):

    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        if user:
            user = authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('/', locals())
        else:
            redirect('/signup', locals())
    else:
        return render(request, 'signup/signup.html', locals())

def signout(request):
    auth.logout(request)
    return redirect('/', locals())
    # return redirect('/signup', locals())
