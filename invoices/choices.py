from django.db import models

class InvoiceStatus(models.TextChoices):

    DRAFT = 'Draft', 'Draft'
    SENT = 'Sent', 'Sent'
    PAID = 'Paid', 'Paid'
    CANCELED = 'Canceled', 'Canceled'