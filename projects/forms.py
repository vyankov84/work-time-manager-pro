from django import forms
from django.forms import ModelForm
from projects.models import Project


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'job_number',
            'description',
            'region',
            'client',
            'project_status',
            'project_manager',
            'assigned_employees',
            'estimated_hours',
            'total_budget',
            'hourly_rate',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'job_number': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'project_status': forms.Select(attrs={'class': 'form-control'}),
            'project_manager': forms.Select(attrs={'class': 'form-control'}),
            'assigned_employees': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'estimated_hours': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.25', 'min': '0'}),
            'total_budget': forms.NumberInput(attrs={'class': 'form-control'}),
            'hourly_rate': forms.NumberInput(attrs={'class': 'form-control'}),
        }

