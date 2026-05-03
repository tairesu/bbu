from django import forms
from directory.models import (
    Business
)

class NewBusinessForm(forms.ModelForm):
    template_name = 'forms/standard.html'

    class Meta:
        model = Business
        fields = [
            'name',
            'email',
            'description',
            'headline',
            'category',
            'website',
            'instagram',
            'logo',
        ]
