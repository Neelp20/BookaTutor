from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'phone', 'address', 'city', 'country']
        widgets = {
            'bio': forms.Textarea(
                attrs={'rows': 3,
                       'placeholder': 'Write something about yourself...'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),

        }
