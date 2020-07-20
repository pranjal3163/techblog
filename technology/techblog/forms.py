from .models.comments import Comments
from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['author', 'text']
