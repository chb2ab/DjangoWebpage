# -*- coding: utf-8 -*-

from django import forms
from uploader.models import Report, Folder

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

class reportEditForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = ('user',)

class folderEditForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ('name',)
