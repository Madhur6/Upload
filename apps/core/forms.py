from django import forms
from .models import Uploaded

class Upload_Form(forms.ModelForm):
    file = forms.FileField(widget=forms.TextInput(attrs={
        'name':'file',
        'type':'file',
        'class':'form-control-sm',
        'multiple':'True',
    }), label='')

    class Meta:
        model = Uploaded
        fields = ['file']