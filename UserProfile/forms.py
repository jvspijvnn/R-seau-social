from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'content': forms.TextInput(attrs={'class': 'bg-transparent max-h-10 shadow-none'}),
            'post': forms.HiddenInput(),
        }