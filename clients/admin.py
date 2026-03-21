from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    list_display = ['name', 'contact_person','country', 'contract_date', 'is_active',]

    search_fields = ['name', 'contact_person', 'contact_email']

    list_filter = ['is_active', 'country']

    ordering = ['-contract_date',]

    list_editable = ['is_active',]
