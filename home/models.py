from django.db import models
class loging(models.Model):
    user_id=models.EmailField( )
    password = models.CharField(max_length=20)
# Create your models here.
