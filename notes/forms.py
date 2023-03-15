from django import forms
from .models import Notes, Semester

class NotesForm(forms.ModelForm):

    semester_num = forms.ChoiceField(choices=Semester.SEMESTER_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pdf'].widget.attrs.update({'class': 'notes-pdf'})

    class Meta:
        model = Notes
        fields = ( 'semester_num', 'subject', 'unit', 'pdf')

        