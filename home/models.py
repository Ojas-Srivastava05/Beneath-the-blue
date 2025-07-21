from django.db import models    

# Create your models here.    
class loging(models.Model):
    user_id = models.EmailField()
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user_id

# Create your models here.
