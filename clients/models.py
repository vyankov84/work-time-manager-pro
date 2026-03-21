from django.core.validators import MinLengthValidator
from django.db import models

from clients.validators import PhoneNumberValidator


class Client(models.Model):

    name = models.CharField(
        max_length=150,
        unique=True,
    )

    contact_person = models.CharField(
        max_length=100,
    )

    country = models.CharField(
        max_length=100,
    )

    contact_email = models.EmailField()

    phone_number = models.CharField(
        max_length=20,
        validators=[
            PhoneNumberValidator(),
            MinLengthValidator(7,'The phone number is too short!')
        ],
        blank=True,
        null=True,
    )

    contract_date = models.DateField(
        blank=True,
        null=True,
    )

    logo = models.ImageField(
        upload_to='clients/',
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name
