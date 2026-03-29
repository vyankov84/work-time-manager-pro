from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from invoices.models import Invoice


class InvoiceSerializer(ModelSerializer):
    project_name = serializers.ReadOnlyField(source='project.name')
    client_name = serializers.ReadOnlyField(source='client.name')

    class Meta:
        model = Invoice
        fields = [
            'id', 'invoice_number', 'project_name', 'client_name',
            'total_amount', 'status', 'issued_date', 'due_date'
        ]