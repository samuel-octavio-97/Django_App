from django import forms
from .models import Image
from django.core.exceptions import ValidationError


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('name', 'image_file')
