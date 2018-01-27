from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=50)

    def __str__(self): # for displaying in admin management
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True) # previous is DateFiled modified

    def __str__(self):
        return "<Blog: %s>"%self.title


