from django import forms
from .models import RadioStation

class RadioStationForm(forms.ModelForm):
    class Meta:
        model = RadioStation
        fields = ['name','description', 'stream_url', 'image', 'category']
