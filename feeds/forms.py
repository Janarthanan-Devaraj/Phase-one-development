from django import forms
from .models import Feed
from django.core.files.storage import FileSystemStorage


class FeedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'id': 'post-img'})

    class Meta:
        model = Feed
        fields = ( 'caption', 'image',)
        widgets = {
            'caption': forms.TextInput(attrs={'id':'post-caption', 'placeholder':'What\'s on your mind, Diana?'}),
        }

        