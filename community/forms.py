# community/forms.py
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'location', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

class PostEditForm(forms.ModelForm):
    new_media = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'multiple': False}),
        label='Add more media'
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'location', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
            'tags': forms.TextInput(attrs={'placeholder': 'comma,separated,tags'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }