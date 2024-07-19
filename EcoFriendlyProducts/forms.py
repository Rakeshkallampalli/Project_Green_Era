from django import forms
from .models import User, UserRating

from django.contrib.auth.forms import UserCreationForm, PasswordResetForm





class UserRatingForm(forms.ModelForm):
    class Meta:
        model = UserRating
        fields = ['rating', 'review_title', 'review_text']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }


class CustomPasswordResetForm:
    pass


class ContactForm:
    pass