from django import forms

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()
    nombre = forms.CharField()

