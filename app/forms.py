# -*- coding: utf-8 -*-
from django import forms
from app.models import *
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput
)


class PersonForm(forms.ModelForm):
    """
    Form that manages the person model fields
    """
    first_name = forms.CharField(widget=TextInput(attrs={
            'class':'form-control input-md',
            'style': 'width: 100%; display: inline;',
        }), required = True)

    last_name = forms.CharField(widget=TextInput(attrs={
            'class':'form-control input-md',
            'style': 'width: 100%; display: inline;',
        }), required = True)

    class Meta:

        model = Person

        fields = [
            'first_name',
            'last_name',
        ]
