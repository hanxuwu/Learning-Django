from django.db import models
from django.utils import timezone  #METHOD_2
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)  # type char
    content = models.TextField()  # type text
    #created_time = models.DateTimeField() #METHOD_1
    created_time = models.DateTimeField(default=timezone.now) #METHOD_2
    last_updated_time =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Article:%s>"%self.title