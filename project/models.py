from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(max_length=254)
    countUser = models.IntegerField(default=0)


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


# user left join project where user.project.id = project.id
