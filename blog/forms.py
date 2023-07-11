from django import forms
from .models import Polygone

class PolygoneForm(forms.ModelForm):
    class Meta:
        model = Polygone
        fields = ('nom', 'polygone')