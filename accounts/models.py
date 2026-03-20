from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.choices import DepartmentType
from accounts.validators import validate_email


class EmployeeUser(AbstractUser):

    first_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    job_title = models.CharField(
        max_length=50,
    )

    email = models.EmailField(
        validators=[validate_email],
        unique=True,
    )

    department = models.CharField(
        max_length=15,
        choices=DepartmentType.choices,
        default=DepartmentType.OTHER,
    )

    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        null=True,
        blank=True
    )

    is_manager = models.BooleanField(
        default=False,
        help_text='Designates whether this user has manager permissions.'
    )


    def __str__(self):
        return f'{self.first_name} {self.last_name} : ({self.username})'
