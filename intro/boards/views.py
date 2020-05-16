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