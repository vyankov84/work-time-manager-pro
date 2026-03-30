from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_invoice_notification_email(invoice_number, total_amount, recipient_email):
    subject = f'New Invoice {invoice_number}'
    message = f'Hi,\n Your latest invoice is now available for the amount of {total_amount}$'

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL or 'wtm-billing@company.com',
        [recipient_email],
        fail_silently=False,
    )

    return f'Email sent to {recipient_email}'
