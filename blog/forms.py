from django import forms
from .models import Post, Form

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
    
class SaveForm(forms.ModelForm):

    class Meta:
        model = Form
        fields = "__all__"