from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Article

# Create your views here.
def article_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    #return HttpResponse("Article id: %s "%article_id)
    except Article.DoesNotExist:
        raise Http404("Not exist")
    return HttpResponse("<h2>Article title: %s</h2><br>Article content: %s "%(article.title,article.content))