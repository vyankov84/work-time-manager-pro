from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

ALLOWED_DOMAINS = [
    'company.com',
    'company.org',
    'company.bg',
    'company.co.uk'
]

@deconstructible
class EmailDomainValidate:

    def __init__(self, message=None):
        self.message = message or 'Please use a valid company email domain!'

    def __call__(self, value):

        if '@' not in value:
            return

        if value.split('@')[1].lower() not in ALLOWED_DOMAINS:
            raise ValidationError(self.message)

