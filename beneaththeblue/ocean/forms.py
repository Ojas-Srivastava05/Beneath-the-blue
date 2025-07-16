from django import forms
from .models import Pledge, Idea, Feedback, Subscriber

class PledgeForm(forms.ModelForm):
    class Meta:
        model = Pledge
        fields = ['name', 'email', 'eliminate_plastics', 'sustainable_seafood', 
                 'join_cleanups', 'reduce_footprint', 'support_conservation', 'personal_promise']
        widgets = {
            'personal_promise': forms.Textarea(attrs={'rows': 4}),
        }

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['name', 'email', 'title', 'description', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback_type', 'message', 'rating']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']