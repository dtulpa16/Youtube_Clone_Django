from django.db import models

class Comment(models.Model):
    video = models.TextField(max_length=100, blank=True,null=True)
    comment = models.CharField(max_length=1000)
    likes = models.IntegerField(null=0)
    dislikes=models.IntegerField(null=0)
# Create your models here.
