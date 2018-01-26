"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path   #new in Django 2.0      
from . import views
from article.views import article_detail # reference
from article.views import article_list # reference

urlpatterns = [
    path('admin/', admin.site.urls),  # www.xxxx.com/admin/
    path('', views.index),  # open the link first page     # www.xxxx.com,then add an method
    # re_path('$',views.index)    Django 1.0 style the same 
    path('article/',include('article.urls')),
]
