from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleSerializer

# Nogada
@require_GET
def article_list_json_1(request):
    articles = Article.objects.all()
    data = []
    for article in articles:
        data.append({
            'article_id' : article.id,
            'title': article.title,
            'content': article.content,
            'created_at': article.created_at,
            'updated_at': article.updated_at,
        })
    
    return JsonResponse(data, safe=False)

# django core serializer
@require_GET
def article_list_json_2(request):
    from django.core import serializers

    articles = Article.objects.all()
    data = serializers.serialize('json', articles)

    return HttpResponse(data, content_type='application/json')

# rest framework
@api_view(['GET'])
def article_list_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)

    # rest_framework의 serializer를 리턴하려면, Reponse를 써야한다.
    return Response(serializer.data)