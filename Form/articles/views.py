from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')  # 가장 최신에 등록한 글을 맨 위로
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        # POST /articles/new => (구) create 함수
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    else:
        # GET /articles/new 
        form = ArticleForm()
    # 공용 context
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request,pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)
