from django.db import models

class Comment(models.Model):
    video = models.CharField(max_length=100, blank=True,null=True)
    comment = models.CharField(max_length=1000)
    likes = models.IntegerField(null=0)
    dislikes=models.IntegerField(null=0)
# Create your models here.

class Reply(models.Model):
    comment_id = models.ForeignKey(Comment, null=True,blank=True,on_delete=models.CASCADE)
    reply = models.CharField(max_length=1000)
