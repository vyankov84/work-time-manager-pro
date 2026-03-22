from django.db import models
from accounts.models import EmployeeUser
from clients.models import Client
from projects.choices import RegionType, ProjectStatus
from projects.validators import validate_job_number_region


class Project(models.Model):

    name = models.CharField(
        max_length=150,
    )

    job_number = models.CharField(
        max_length=10,
        unique=True,
        help_text='Format: 111XXXXXXX for EMEA, 222XXXXXXX for APAC, etc.'
    )

    description = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    region = models.CharField(
        max_length=10,
        choices=RegionType.choices,
    )

    client = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    project_status = models.CharField(
        max_length=10,
        choices=ProjectStatus.choices,
        default=ProjectStatus.PENDING
    )

    project_manager = models.ForeignKey(
        EmployeeUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_projects'
    )

    assigned_employees = models.ManyToManyField(
        EmployeeUser,
        blank=True,
        related_name='assigned_projects'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    estimated_hours = models.PositiveIntegerField(
        default=0
    )

    total_budget = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )


    def clean(self):
        super().clean()
        validate_job_number_region(self.job_number, self.region)


    def __str__(self):
        return f'{self.name} : {self.job_number}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
