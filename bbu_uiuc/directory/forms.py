from django import forms
from directory.models import (
    Business
)


class NewBusinessForm(forms.ModelForm):
    
    class Meta:
        model = Business
        fields = '__all__'
