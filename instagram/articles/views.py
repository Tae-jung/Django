from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:detail', article.pk)
        messages.warning(request, '폼을 다시 확인 후 제출해주세요.')
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request,'articles/forms.html', context)

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)
