from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Community(models.Model):
    title = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='communities')
    link = models.URLField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    


class Quiz(models.Model):
    question = models.CharField(max_length=255)
    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    op3 = models.CharField(max_length=200)
    op4 = models.CharField(max_length=200)
    options = models.IntegerField()
    score = models.IntegerField()

    def __str__(self):
        return self.question