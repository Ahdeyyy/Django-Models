from re import T
from django.db import models
import django

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(django.contrib.auth.get_user_model(),on_delete= models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

