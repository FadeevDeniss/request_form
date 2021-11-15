from django import forms
from message.models import Credentials

class CredentialForm(forms.ModelForm):
    class Meta:
        model = Credentials
        fields = ['name', 'description', 'email', 'checkbox']
