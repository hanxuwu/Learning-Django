from django.urls import path  
from . import views

urlpatterns = [
    # localhost:8000/article/
    path('<int:article_id>',views.article_detail,name="article_detail"), # name could named by yourself
    # localhost:8000/article/1
    path('',views.article_list,name="article_list"), # add article_list
]