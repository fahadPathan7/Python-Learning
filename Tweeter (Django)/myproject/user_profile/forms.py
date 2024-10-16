from django import forms
from . models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'address', 'nationality', 'date_of_birth', 'image']