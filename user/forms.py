from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import User, AcademicsInfo, CompanyInfo

class StepZeroForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
    TYPE_CHOICES= [
    ('student', 'Student'),
    ('alumni', 'Alumni'),
    ]    
    type = forms.CharField(label='You are?', widget=forms.RadioSelect(choices=TYPE_CHOICES))
                           
    class Meta:
        model = User
        fields = ['type','email', 'password1', 'password2']

class StepOneForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True

    dob = forms.DateField(label="Date Of Birth", widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'dob', 'gender']
        exclude = ['password1', 'password2']

class StepTwoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True

    roll_number = forms.CharField(max_length=7, error_messages={
        'unique': 'This roll number has already been registered.'
    })
    class Meta:
        model = AcademicsInfo
        fields = '__all__'
        exclude = ['user']


class StepThreeForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True

    class Meta:
        model = CompanyInfo
        fields = '__all__'
        exclude = ['user']


class EditUserProfile(ModelForm):

    class Meta:
        model = User
        fields = ['profile_pic', 'profile_cover', 'first_name', 'last_name','username', 'email', 'dob', 'gender']
        widgets = {
            'dob':  forms.DateInput(attrs={'type': 'date'})
        }