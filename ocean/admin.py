from django.contrib import admin

# Register your models here.
from ocean.models import Pledge, Idea, Feedback, Subscriber

admin.site.register(Pledge)
admin.site.register(Idea)
admin.site.register(Feedback)
admin.site.register(Subscriber)

