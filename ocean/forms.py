from django import forms
from .models import Pledge, Idea, Feedback

class PledgeForm(forms.ModelForm):
    class Meta:
        model = Pledge
        fields = "__all__" 

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = "__all__" 

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__" 
