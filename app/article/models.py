from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from time import time

def get_upload_file_name(instance, filename):
    return "%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.
class Article(models.Model):
    
    class Meta():
        db_table = 'article'
    
    article_title = models.CharField(max_length = 200)
    article_text = models.TextField()
    article_date = models.DateTimeField(default=datetime.now)
    article_likes = models.IntegerField(default=0)
    thubnail = models.FileField(upload_to=get_upload_file_name)
        
    def __str__(self):
        return self.article_title
    
    
class Comments(models.Model):
    
    class Meta():
        db_table = 'comments'
    
    comments_date = models.DateTimeField(default=datetime.now)    
    comments_text = models.TextField(verbose_name="Your comment")
    comments_article = models.ForeignKey(Article)
    comments_from = models.ForeignKey(User)
    
class likes_table(models.Model):

    class Meta():
        db_table = 'likes'
        
    likes_from = models.IntegerField()
    likes_for = models.IntegerField()
