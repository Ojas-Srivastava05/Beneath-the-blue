from django.contrib import admin
from home.models import  *
# Register your models here.
class log(admin.ModelAdmin):
    list_display=('user_id','password')
admin.site.register(loging,log)
