from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from accounts.forms import EmployeeCreationForm, EmployeeEditForm
from accounts.models import EmployeeUser


class EmployeeListView(LoginRequiredMixin, ListView):
    model = EmployeeUser
    context_object_name = 'employees'
    template_name = 'accounts/employee-list.html'


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = EmployeeUser
    context_object_name = 'employee'
    template_name = 'accounts/employee-details.html'


class EmployeeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EmployeeUser
    form_class = EmployeeEditForm
    template_name = 'accounts/employee-update.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    raise_exception = True

    def test_func(self):
        return self.request.user.is_manager

    def get_success_url(self):
        return reverse_lazy('accounts:employee-details', kwargs={'pk':self.object.pk})


class EmployeeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EmployeeUser
    template_name = 'accounts/employee-confirm-delete.html'
    success_url = reverse_lazy('accounts:employee-list')

    raise_exception = True

    def test_func(self):
        return self.request.user.is_manager


class LoginEmployeeView(LoginView):
    template_name = 'accounts/login.html'


class LogoutEmployeeView(LogoutView):
    pass


class RegisterEmployeeView(CreateView):
    form_class = EmployeeCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
