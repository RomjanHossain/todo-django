from django import forms
from .models import Lists


class ListForm(forms.ModelForm):
    class Meta:
        model = Lists
        fields = ('item', 'completed')
