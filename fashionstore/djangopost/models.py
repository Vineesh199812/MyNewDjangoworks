from django.db import models

# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=120)
    author=models.CharField(max_length=120)
    liked_by=models.CharField(max_length=120)
