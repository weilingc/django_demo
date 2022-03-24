from urllib.error import HTTPError

from django.contrib import auth, messages  # django內建使用者系統
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm  # django內建註冊表單模型
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from . import forms


def show_myorders(request):
    return render(request, 'myorders.html', locals())

def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '帳號尚未啟用')
            else:
                messages.add_message(request, messages.WARNING, '登入失敗')
        else:
            messages.add_message(request, messages.WARNING, '請檢查輸入欄位內容')
    else:
        login_form = forms.LoginForm()
    return render(request, 'accounts/login.html', locals())

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html', locals())
