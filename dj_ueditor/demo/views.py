# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from  demo.models import Article


# Create your views here.
def index(request):
    article_list = Article.objects.all().values_list('id', 'title')
    # article_list = Article.objects.all()
    return render(request, 'index.html', {'article_list': article_list})

def detail(request,tid):
    article = Article.objects.get(id=tid)
    contenxt=str(article.context)
    return render(request, 'detail.html',locals())
