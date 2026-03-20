from django.core.exceptions import ValidationError

ALLOWED_DOMAINS = [
    'company.com',
    'company.org',
    'company.bg',
    'company.co.uk'
]

def validate_email(value):

    if '@' not in value:
        return

    if value.split('@')[1] not in ALLOWED_DOMAINS:
        raise ValidationError('The domain should consist company')
