from django.urls import path
from . import views





#http://localhost:8000

# need start with blog
urlpatterns = [
    #http://localhost:8000/blog/
    path('',views.blog_list,name='blog_list'),
    #http://localhost:8000/blog/1
    path('<int:blog_pk>',views.blog_detail,name="blog_detail"),
    path('type/<int:blog_type_pk>',views.blogs_with_type,name="blogs_with_type"),
    
]