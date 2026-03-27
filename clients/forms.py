from django import forms
from django.forms import ModelForm
from clients.models import Client


class ClientCreateForm(ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'contact_person',
            'country',
            'contact_email',
            'phone_number',
            'contract_date',
            'logo'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'contract_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }

