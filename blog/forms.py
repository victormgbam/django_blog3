from .models import Comment
from django import forms


class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
