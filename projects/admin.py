from django.contrib import admin
from projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'job_number',
        'region','client',
        'project_status',
        'project_manager',
        'display_team',
        'total_hours_worked',
        'estimated_hours',
        'hourly_rate'
    ]

    search_fields = ['name', 'job_number', 'client__name']

    list_editable = ['project_status']

    filter_horizontal = ['assigned_employees']

    list_filter = ['region', 'project_status']

    def display_team(self, obj):
        assigned_pms = obj.assigned_employees.all()
        if not assigned_pms:
            return '-'
        return ', '.join([f"{pm.first_name} {pm.last_name}" for pm in assigned_pms])

