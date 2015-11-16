# -*- coding: utf-8 -*-

from django import forms
from uploader.models import Report

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

class reportEditForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = ('user',)
