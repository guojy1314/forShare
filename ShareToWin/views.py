from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'webshare/index.html', context={
        'title': '分享为赢首页',
        'welcome': '欢迎访问分享为赢首页'
    })
