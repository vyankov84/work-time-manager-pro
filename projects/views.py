from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView, TemplateView

from accounts.models import EmployeeUser
from activities.models import Activity
from projects.forms import ProjectCreateForm
from projects.models import Project


class ProjectCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'projects/project-create.html'
    success_url = reverse_lazy('projects:projects-list')

    raise_exception = True

    def test_func(self):
        return self.request.user.is_manager


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'projects/project-delete.html'
    success_url = reverse_lazy('projects:projects-list')

    raise_exception = True
    def test_func(self):
        return self.request.user.is_manager

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ProjectCreateForm(instance=self.object)

        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['placeholder'] = ''

        context['form'] = form
        return context

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'projects/project-update.html'

    raise_exception = True
    def test_func(self):
        return self.request.user.is_manager

    def get_success_url(self):
        return reverse_lazy('projects:project-details', kwargs = {'pk': self.object.pk})

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/projects-list.html'


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'projects/project-details.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'projects/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_projects'] = Project.objects.count()
        context['total_employees'] = EmployeeUser.objects.count()

        context['recent_activities'] = Activity.objects.select_related(
            'employee', 'project'
        ).order_by('-date', '-created_at')[:5]

        context['projects_overview'] = Project.objects.filter(
            project_status='ACTIVE'
        ).order_by('-created_at')[:8]

        context['page_title'] = 'Dashboard'

        return context