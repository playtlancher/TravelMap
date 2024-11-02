from django.forms import ModelForm
from django.forms.widgets import Input, Textarea
from route.models import Route


class AddRouteForm(ModelForm):
    class Meta:
        model = Route
        fields = ['name', 'description', "short_description"]
        widgets = {
            "name": Input(attrs={
                'id': 'routeName',
                'class': 'form-control',
                'type': 'text',
                'name': 'routeName',
                'placeholder': 'Name',
            }),
            "description": Textarea(attrs={
                'id': 'routerDescription',
                'class': 'form-control',
                'type': 'text',
                'name': 'routerDescription',
                'placeholder': 'Description',
            }),
            "short_description": Textarea(attrs={
                'id': 'shortDescription',
                'class': 'form-control',
                'type': 'text',
                'name': 'shortDescription',
                'placeholder': 'Short description',
            })
        }
