from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from activities.models import Activity
from invoices.forms import InvoiceCreateForm
from invoices.models import Invoice


class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoice
    template_name = 'invoices/invoices-list.html'
    context_object_name = 'invoices'
    paginate_by = 10


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    model = Invoice
    template_name = 'invoices/invoice-details.html'
    context_object_name = 'invoice'



class InvoiceCreateView(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = Invoice
    form_class = InvoiceCreateForm
    template_name = 'invoices/invoice-create.html'
    success_url = reverse_lazy('invoices:invoices-list')

    raise_exception = True
    def test_func(self):
        return self.request.user.is_manager

    def form_valid(self, form):
        response = super().form_valid(form)
        invoice = self.object

        activities = Activity.objects.filter(project=invoice.project, invoiced_in__isnull=True)
        invoice.activities.set(activities)

        total_hours = sum(act.hours_worked for act in activities)
        invoice.total_amount = total_hours * invoice.project.hourly_rate
        invoice.save()

        return response



class InvoiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Invoice
    form_class = InvoiceCreateForm
    template_name = 'invoices/invoice-update.html'

    raise_exception = True
    def test_func(self):
        return self.request.user.is_manager

    def form_valid(self, form):
        response = super().form_valid(form)
        invoice = self.object

        activities = invoice.activities.all()
        if activities.exists():
            total_hours = sum(act.hours_worked for act in activities)
            invoice.total_amount = total_hours * invoice.project.hourly_rate
            invoice.save()

        return response

    def get_success_url(self):
        return reverse_lazy('invoices:invoice-details', kwargs={'pk': self.object.pk})



class InvoiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Invoice
    template_name = 'invoices/invoice-delete.html'
    success_url = reverse_lazy('invoices:invoice-list')

    raise_exception = True
    def test_func(self):
        return self.request.user.is_manager

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = InvoiceCreateForm(instance=self.object)

        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['placeholder'] = ''

        context['form'] = form
        return context
