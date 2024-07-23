from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    image = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'image']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']  # C

