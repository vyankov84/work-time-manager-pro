from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from accounts.forms import EmployeeCreationForm
from accounts.models import EmployeeUser


class EmployeeListView(LoginRequiredMixin, ListView):
    model = EmployeeUser
    context_object_name = 'employees'
    template_name = 'accounts/employee-list.html'


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = EmployeeUser
    context_object_name = 'employee'
    template_name = 'accounts/employee_details.html'


class LoginEmployeeView(LoginView):
    template_name = 'accounts/login.html'


class LogoutEmployeeView(LogoutView):
    pass


class RegisterEmployeeView(CreateView):
    form_class = EmployeeCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
