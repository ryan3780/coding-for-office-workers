from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
    article_list = Article.objects.all()
    ctx = {
    "article_list" : article_list
    }
    return render(request, "index.html", ctx)
