from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from accounts.models import EmployeeUser
from activities.forms import ActivityCreateForm
from activities.models import Activity
from projects.models import Project


class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    template_name = 'activities/activity-create.html'
    form_class = ActivityCreateForm
    success_url = reverse_lazy('projects:projects-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class ActivityListView(LoginRequiredMixin, ListView):
    model = Activity
    context_object_name = 'activities'
    template_name = 'activities/activities-list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.is_manager:
            return queryset.filter(employee=self.request.user)
        else:
            emp_id = self.request.GET.get('employee')
            if emp_id:
                queryset = queryset.filter(employee_id=emp_id)

        pr_id = self.request.GET.get('project')
        if pr_id:
            queryset = queryset.filter(project_id=pr_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['all_projects'] = Project.objects.all()
        if self.request.user.is_manager:
            context['all_employee'] = EmployeeUser.objects.all()

        context['total_hours'] = self.get_queryset().aggregate(Sum('hours_worked'))['hours_worked__sum'] or 0
        return context


class ActivityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Activity
    form_class = ActivityCreateForm
    template_name = 'activities/activity-update.html'
    success_url = reverse_lazy('activities:activities-list')

    raise_exception = True

    def test_func(self):
        return self.request.user.is_manager


class ActivityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Activity
    template_name = 'activities/activity-delete.html'
    success_url = reverse_lazy('activities:activities-list')

    raise_exception = True
    def test_func(self):
        return self.request.user.is_manager

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ActivityCreateForm(instance=self.object)

        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['placeholder'] = ''

        context['form'] = form

        return context

