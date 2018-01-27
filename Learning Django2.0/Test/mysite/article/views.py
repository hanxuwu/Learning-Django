from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Article

# Create your views here.
def article_detail(request, article_id):
    #try:
    #article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article,pk=article_id)
#return HttpResponse("Article id: %s "%article_id)
    context={}
    context['article_obj']=article   # dictionary
    #return render(request,"article_detail.html",context) # use template
    return render_to_response("article_detail.html",context) # the same as last line 
    #except Article.DoesNotExist:
        #raise Http404("Not exist")
    #return HttpResponse("<h2>Article title: %s</h2><br>Article content: %s "%(article.title,article.content))

def article_list(request):
    #articles = Article.objects.all()
    articles = Article.objects.filter(is_deleted=False) # filter the deletedone
    context={}
    context['articles'] = articles
    return render_to_response("article_list.html",context)
