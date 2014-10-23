from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def login(request):
    login_error = ""
    nexturl = request.GET.get('next', '/')
    try:
        username = request.POST['login_username']
        password = request.POST['login_password']
        nexturl = request.POST['next']

        if 'submit_registration' in request.POST:
            if not username:
                login_error = "You must supply a username to register."
            elif not password:
                login_error = "You must supply a password to register."
            else:
                user = User.objects.create_user(username, '', password)
                user.save()
                user = authenticate(username=username, password=password)
                auth_login(request, user)
                return HttpResponseRedirect(request.POST.get('next', '/'))
        elif 'submit_login' in request.POST:
            if not username:
                login_error = "You must supply a username to log in."
            elif not password:
                login_error = "You must supply a password to log in."
            else:
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return HttpResponseRedirect(request.POST.get('next', '/'))
                else:
                    login_error = "Invalid username or password."
    except KeyError:
        pass

    return render(request, "zlogio/login.html", {'login_error': login_error, 'next': nexturl})

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
