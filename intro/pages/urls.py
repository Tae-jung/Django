from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('hello/', views.hello),
    path('lotto/', views.lotto),
    path('iam/', views.iam),
    path('lunch/', views.lunch),
    path('hi/<str:name>/', views.hi), # variable routing/name변수로
    path('add/<int:A>/<int:B>/', views.add),
    path('posts/<int:number>/', views.posts),
]