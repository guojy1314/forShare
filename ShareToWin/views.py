from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

# Create your views here.
from django.http import HttpResponse


def index(request):
    pass
    return render(request, 'webshare/index.html')


def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'webshare/login.html', locals())

    login_form = UserForm()
    return render(request, 'webshare/login.html', locals())


def register(request):
    pass
    return render(request, 'webshare/register.html')


def logout(request):
    pass
    return redirect('webshare/index/')
