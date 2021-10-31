from django import forms
from django.db.models import fields    
from .models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']



