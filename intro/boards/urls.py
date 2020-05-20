from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('complete/', views.complete),
    path('ping/', views.ping),
    path('pong/', views.pong),
]