from django.forms import ModelForm
from django.forms.widgets import Textarea

from comment.models import Comment


class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": Textarea(attrs={
                'id': 'shortDescription',
                'class': 'form-control',
                'type': 'text',
                'name': 'shortDescription',
                'placeholder': 'Comment text',
            })
        }
