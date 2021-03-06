from django.contrib import admin
from .models import Article
# Register your models here.

# Admin Site를 이쁘게
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at')

# 어드민 사이트에 등록해줘
admin.site.register(Article, ArticleAdmin)