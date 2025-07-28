from django.db import models

# Create your models here.
class endangered_species(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
class EndangeredSpecies(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    audio = models.FileField(upload_to='audios/')
    des=models.TextField(default='No description available')
    threat = models.ForeignKey(endangered_species, on_delete=models.CASCADE, related_name='endangered_species')
    url=models.URLField(blank=True, null=True)