from django.contrib import admin

# Register your models here.
from ocean.models import Pledge, Idea, Feedback

admin.site.register(Pledge)
admin.site.register(Idea)
admin.site.register(Feedback)

