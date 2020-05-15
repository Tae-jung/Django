from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def hello(request):
    return render(request, 'pages/hello.html')

def lotto(request):
    pick = random.sample(range(1,46), 6)
    context = {
        'pick' : pick
    }
    return render(request, 'pages/lotto.html', context)

def iam(request):
    return render(request, 'pages/iam.html')

def lunch(request):
    menus = ['피자', '햄버거', '설렁탕', '마라탕', '삼계탕']
    menu = random.choice(menus)
    context = {
        'menu' : menu,
        'menus' : menus,
    }
    return render(request, 'pages/lunch.html', context)

def hi(request, name):
    context = {
        'name' : name
    }
    return render(request, 'pages/hi.html', context)

def add(request, A, B):
    result = A + B
    context = {
        'result' : result
    }
    return render(request, 'pages/add.html', context)

def posts(request, number):
    content = 'Life is short, you need Python'
    replies = ['Good', 'Great', 'Me too']
    no_replies = []
    user = 'admin'
    context = {
        'number' : number,
        'content' : content,
        'replies' : replies,
        'no_replies' : no_replies,
        'user' : user
    }
    return render(request, 'pages/posts.html', context)