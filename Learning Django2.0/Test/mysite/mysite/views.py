from django.http import HttpResponse 

def index(request):    # request: argument
    return HttpResponse("Hello,world")  #return string