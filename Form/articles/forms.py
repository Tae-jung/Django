from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length='100',
        label='제목',
        help_text='제목은 100자이내로 작성하세요',
        widget=forms.TextInput(
            attrs={
                'class': 'my-input',
                'placeholder': '제목 입력',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        help_text='자유롭게 작성해주세요.',
        widget=forms.Textarea(
            attrs={
                'row': 5,
                'col' : 50,
            }
        )
    )
    class Meta:
        model = Article
        fields = ['title', 'content']


# 중복 제거 위해 Form 대신 Model을 상속받은 ModelForm사용
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     content = forms.CharField(widget=forms.Textarea)