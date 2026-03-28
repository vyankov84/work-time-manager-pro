from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from accounts.models import EmployeeUser
from projects.choices import ProjectStatus
from projects.models import Project


class Activity(models.Model):

    employee = models.ForeignKey(
        EmployeeUser,
        on_delete=models.CASCADE,
        related_name='activities',
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='activities',
    )

    task_name = models.CharField(
        max_length=150,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    date = models.DateField(
        help_text="The day the work was performed",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    hours_worked = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(0.25, message='Minimum work time is 15 minutes'),
            MaxValueValidator(24, message='You cannot work more than 24 hours in a day')
        ],
        help_text='Total time spent (7.5 for 7h 30min)',
    )

    class Meta:
        ordering = ['-date','-created_at']
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def clean(self):
        super().clean()

        if not hasattr(self, 'employee') or self.employee is None:
            return

        if self.project.project_status != ProjectStatus.ACTIVE:
            raise ValidationError(
                f'The project {self.project.name} is currently {self.project.project_status}. '
                f'Activities can be added only to Active projects'
            )

        is_assigned = self.project.assigned_employees.filter(id=self.employee.id).exists()
        is_manager = self.project.project_manager == self.employee

        if not is_assigned and not is_manager:
            raise ValidationError(f'Employee {self.employee} is not assigned for {self.project.name}.')

    def __str__(self):
        return f'{self.task_name} - {self.employee.first_name} {self.employee.last_name} ({self.date})'

