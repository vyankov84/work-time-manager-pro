from django.contrib import admin
from invoices.models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):

    list_display = [
        'invoice_number',
        'project',
        'client',
        'issued_date',
        'status',
        'all_activities'
    ]

    list_filter = ['status', 'issued_date', 'project']

    search_fields = ['invoice_number', 'project__name', 'client__name']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('activities')

    def all_activities(self, obj):
        all_activities = obj.activities.all()
        if not all_activities:
            return 'No activities'

        return ', '.join([str(act.task_name) for act in all_activities])
