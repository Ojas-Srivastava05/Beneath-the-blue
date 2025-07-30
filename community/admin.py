from django.contrib import admin

# Register your models here.
from .models import *

# loging  display
class log(admin.ModelAdmin):
    list_display=('user_id','password')
admin.site.register(loging,log)
# Register the Community model with the admin site

# comminity section
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')
admin.site.register(Category,CategoryAdmin)

class CommunityAdmin(admin.ModelAdmin):
    list_display = ('title','category','description')
admin.site.register(Community, CommunityAdmin)

# Register the Question, Option, and QuizResult models with the admin site
class QuestionAdmin(admin.ModelAdmin):
    list_display = ( 'question', 'op1', 'op2', 'op3', 'op4', 'answer')
admin.site.register(Quiz, QuestionAdmin)

#  the Threat model  section
class ThreatAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
admin.site.register(Threat, ThreatAdmin)

#  endangered species section
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'detailed_description', 'image', 'wikipedia_link', 'related_threat', 'implementation_steps', 'benefits', 'created_at')
admin.site.register(Solution, SolutionAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'file', 'author', 'created_at', 'updated_at','like_count')
admin.site.register(Post, PostAdmin)

class commnetAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at')
admin.site.register(Comment, commnetAdmin)