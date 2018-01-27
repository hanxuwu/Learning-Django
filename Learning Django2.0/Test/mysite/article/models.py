from django.db import models
from django.utils import timezone  #METHOD_2
from django.contrib.auth.models import User # add author

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)  # type char
    content = models.TextField()  # type text
    #created_time = models.DateTimeField() #METHOD_1
    created_time = models.DateTimeField(default=timezone.now) #METHOD_2
    last_updated_time =  models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1)  
    is_deleted = models.BooleanField(default=False)
    read_num = models.IntegerField(default=0)

    def __str__(self):
        return "<Article:%s>"%self.title