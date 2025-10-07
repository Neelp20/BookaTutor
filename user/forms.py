from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_type', 'bio', 'phone', 'location', 'subjects', 'profile_image']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }
