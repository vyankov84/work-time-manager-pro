from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from clients.forms import ClientCreateForm
from clients.models import Client


class ClientCreate(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    form_class = ClientCreateForm
    template_name = 'clients/client-create.html'
    success_url = reverse_lazy('clients:clients-list')

    raise_exception = True

    def test_func(self):
        return self.request.user.is_manager


class ClientUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Client
    form_class = ClientCreateForm
    template_name = 'clients/client-update.html'
    success_url = reverse_lazy('clients:clients-list')

    raise_exception = True

    def test_func(self):
        return self.request.user.is_manager


class ClientDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    template_name = 'clients/client-confirm-delete.html'
    success_url = reverse_lazy('clients:clients-list')

    raise_exception = True

    def test_func(self):
        return self.request.user.is_manager

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ClientCreateForm(instance=self.object)

        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['placeholder'] = ''

        context['form'] = form
        return context

class ClientList(LoginRequiredMixin, ListView):
    model = Client
    context_object_name = 'clients'
    template_name = 'clients/clients-list.html'


class ClientDetails(LoginRequiredMixin, DetailView):
    model = Client
    context_object_name = 'client'
    template_name = 'clients/client-details.html'



