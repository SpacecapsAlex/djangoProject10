from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(max_length=254)
    countUser = models.IntegerField(default=0)
