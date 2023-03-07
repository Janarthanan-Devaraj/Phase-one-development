from django.forms import ModelForm
from .models import Thread

class ThreadForm(ModelForm):
    class Meta:
        fields = '__all__'
        exclude = ['host', 'participants']