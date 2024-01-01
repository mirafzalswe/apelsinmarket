from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from user.models import Customer


class RegistUserForm(UserCreationForm):
    username = forms.CharField(label="login", widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput(attrs={'class':'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1','password2']
        widgets = {
            'email': forms.TextInput(attrs={'class':'form-input'}),
            'first_name' : forms.TextInput(attrs={'class':'form-input'}),
            'last_name' : forms.TextInput(attrs={'class':'form-input'})
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("This email already exists")
        return email


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['avatar', 'about']