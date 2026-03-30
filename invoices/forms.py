from django import forms
from django.forms import ModelForm
from invoices.models import Invoice
from django.utils import timezone


class InvoiceCreateForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'project', 'due_date', 'status']

        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'invoice_number': forms.TextInput(attrs={'placeholder': 'INV-2026-001', 'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < timezone.now().date():
            raise forms.ValidationError('The end date cannot be in the past')
        return due_date

