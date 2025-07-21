from django.contrib import admin

# Register your models here.
from .models import *

# Register the Community model with the admin site
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')
admin.site.register(Category,CategoryAdmin)

class CommunityAdmin(admin.ModelAdmin):
    list_display = ('title','category','description')
admin.site.register(Community, CommunityAdmin)

# Register the Question, Option, and QuizResult models with the admin site
class QuestionAdmin(admin.ModelAdmin):
    list_display = ( 'question', 'op1', 'op2', 'op3', 'op4', 'score')
admin.site.register(Quiz, QuestionAdmin)
 