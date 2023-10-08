from django import forms
from .models import Mails


class WriteMailForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput)
    body = forms.CharField(label='Body', max_length=1000, widget=forms.Textarea)
    class Meta:
        model = Mails
        fields = ('recipient', 'subject', 'body', 'status')

