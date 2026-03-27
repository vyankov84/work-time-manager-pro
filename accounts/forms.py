from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


UserModel = get_user_model()

BOOTSTRAP_WIDGET_ATTRS = {'class': 'form-control'}

class EmployeeCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }

class EmployeeEditForm(ModelForm):
    class Meta:
        model = UserModel
        fields = [
            'email',
            'first_name',
            'last_name',
            'job_title',
            'department',
            'profile_picture',
            'is_manager',
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Designer'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. UI/UX'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'is_manager': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }