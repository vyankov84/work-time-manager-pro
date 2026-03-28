from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from activities.forms import ActivityCreateForm
from activities.models import Activity


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
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_hours'] = self.get_queryset().aggregate(Sum('hours_worked'))['hours_worked__sum'] or 0
        return context