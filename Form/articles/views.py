from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')  # 가장 최신에 등록한 글을 맨 위로
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)
