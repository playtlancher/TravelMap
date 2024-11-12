from django.forms import ModelForm
from django.forms.widgets import Textarea

from comment.models import Comment


class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": Textarea(attrs={
                'id': 'comment-content',
                'class': 'form-control',
                'type': 'text',
                'name': 'comment-content',
                'placeholder': 'Add a comment...',
                'onfocus': 'showButton()',
                'onfocusout': 'hideButton()',
                'rows': '3'
            })
        }
