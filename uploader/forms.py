# -*- coding: utf-8 -*-

from django import forms
from uploader.models import Report, Folder, Group2


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

class groupEditForm(forms.ModelForm):
    class Meta:
        model = Group2
        exclude = ('creator', 'reports', 'permissions',)
