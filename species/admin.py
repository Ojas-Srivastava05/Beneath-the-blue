from django.contrib import admin
from .models import *
# Register your models here.
class  endangered_speciesAdmin(admin.ModelAdmin):
    list_display = ('title',)   
admin.site.register(endangered_species, endangered_speciesAdmin)

class EndangeredSpeciesAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'audio', 'des', 'threat', 'url')  
admin.site.register(EndangeredSpecies, EndangeredSpeciesAdmin)