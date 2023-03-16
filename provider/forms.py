from django import forms
from .models import Provider


# class ProviderForm(forms.ModelForm):
#     name = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "form-control",
#         "placeholder": "name"
#     }))
#     desc = forms.CharField(widget=forms.TextInput(attrs={
#         'type': "number",
#         "class": "form-control",
#         "placeholder": "desc"
#     }))
#
#     price = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "form-control",
#         "placeholder": "price"
#     }))
#
#     class Meta:
#         model = Provider
#         fields = [
#             'name', 'desc', 'price'
#         ]