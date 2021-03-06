from django.shortcuts import render

def index(request):
    return render(request, 'boards/index.html')

def new(request):
    return render(request, 'boards/new.html')

def complete(request):
    # request는 요청과 관련된 정보들이 담긴 객체이다.
    title = request.GET.get('title')
    content = request.GET.get('content')
    context = {
        'title' : title,
        'content' : content,
    }
    return render(request, 'boards/complete.html', context)


def ping(request):
    return render(request, 'boards/ping.html')

def pong(request):
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request, 'boards/pong.html', context)