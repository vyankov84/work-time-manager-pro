from rest_framework import permissions
from rest_framework.generics import ListAPIView
from invoices.models import Invoice
from invoices.serializers import InvoiceSerializer


class InvoiceListAPIView(ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]