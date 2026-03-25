from django.contrib import admin
from activities.models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):

    list_display = ['project', 'date','employee','hours_worked','task_name']

    list_filter = ['project','employee','date']

    search_fields = ['task_name','employee__first_name', 'employee__last_name', 'project__name']

    date_hierarchy = 'date'

