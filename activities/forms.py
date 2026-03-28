from django import forms
from django.db.models import Q
from django.forms import ModelForm
from activities.models import Activity
from projects.choices import ProjectStatus
from projects.models import Project


class ActivityCreateForm(ModelForm):
    class Meta:
        model = Activity
        fields = [
            'project',
            'task_name',
            'date',
            'hours_worked',
            'description',
        ]

        widgets = {
            'date': forms.DateTimeInput(attrs={'type':'date', 'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-select'}),
            'task_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Worked on...'}),
            'hours_worked': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.25', 'min': '0.25'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['project'].queryset = Project.objects.filter(
                project_status=ProjectStatus.ACTIVE
            ).filter(
                Q(assigned_employees=user) | Q(project_manager=user)
            ).distinct()