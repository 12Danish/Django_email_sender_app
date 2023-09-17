from django import forms
from .models import Mails


class WriteMailForm(forms.Form):
    recipient = forms.EmailField(label='To', max_length='150')
    subject = forms.CharField(label='Subject', max_length='200')
    body = forms.CharField(label='Body', max_length=1000, widget=forms.Textarea)
    status = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Mails
        fields = ('recipient', 'subject', 'body', 'status')
