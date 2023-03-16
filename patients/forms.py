from django import forms
from .models import PatientDemo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PatientForm(forms.ModelForm):
    name_first = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "First Name"
    }))
    name_last = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Last Name"
    }))

    dob = forms.DateField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "D.O.B"
    }))

    sex = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Sex"
    }))

    race = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Race"
    }))

    class Meta:
        model = PatientDemo
        fields = [
            'name_first', 'name_last', 'dob',
            'sex', 'race'
        ]