from django.core import validators
from django import forms
from .models import contacts
from django.core.exceptions import ValidationError


class ContactSearch(forms.ModelForm):
    class Meta:
        model = contacts
        fields = ['name']