from django.db import models
from django.contrib.auth.models import User

# loging
class loging(models.Model):
    user_id = models.EmailField()
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user_id

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
    answer = models.IntegerField()

    def __str__(self):
        return self.question

class Threat(models.Model):
    image = models.ImageField(upload_to='threats/', blank=True, null=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    # solution = models.TextField()
    url = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.title

class Solution(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    detailed_description = models.TextField()
    image = models.ImageField(upload_to='solutions/', blank=True, null=True)
    wikipedia_link = models.URLField(blank=True, null=True)
    related_threat = models.ForeignKey(Threat, on_delete=models.CASCADE, related_name='solutions')
    implementation_steps = models.TextField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

