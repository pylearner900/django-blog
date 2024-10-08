from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","desc","image"]
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Title"
        self.fields['desc'].widget.attrs['placeholder'] = "Description"