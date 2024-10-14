from django import forms
from .models import ChaVarity

class ChaVarityForm(forms.Form):
    cha_varity = forms.ModelChoiceField(queryset=ChaVarity.objects.all(), label="Select Cha Variety", empty_label=None) # This will create a dropdown list of all the cha varieties.