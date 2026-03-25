from django.db import models
from activities.models import Activity
from clients.models import Client
from invoices.choices import InvoiceStatus
from projects.models import Project


class Invoice(models.Model):

    invoice_number = models.CharField(
        max_length=20,
        unique=True,
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='invoices'
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name='invoices'
    )

    activities = models.ManyToManyField(
        Activity,
        related_name='invoiced_in',
        blank=True
    )

    issued_date = models.DateField(auto_now_add=True)

    due_date=models.DateField()

    status = models.CharField(
        max_length=10,
        choices=InvoiceStatus.choices,
        default=InvoiceStatus.DRAFT,
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )

    def __str__(self):
        return f'Invoice {self.invoice_number} : {self.client} - {self.project}'

    class Meta:
        ordering = ['-issued_date']

