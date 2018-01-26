from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)  # type char
    content = models.TextField()  # type text

    def __str__(self):
        return "<Article:%s>"%self.title