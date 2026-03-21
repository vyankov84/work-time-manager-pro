from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class PhoneNumberValidator:

    def __init__(self, message=None):
        self.message = message or 'The phone number should contain only digits'

    def __call__(self, value):
        if not value:
            return

        if not value.isdigit():
            raise ValidationError(self.message)
