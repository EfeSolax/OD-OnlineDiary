from django import forms
from .models import BlogModel

class BlogForm(forms.ModelForm):
    class Meta:
        style_title = """
width: 750px; 
height: 45px; 
margin-bottom: 25px;
font-size: 22px;
    """


        model = BlogModel
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Başlık', "style": style_title}),
            'content': forms.Textarea(attrs={'rows': 17, 'placeholder': 'İçerik', 'class': 'my-custom-class autosize'}),
        }
        



    