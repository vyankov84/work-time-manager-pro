from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import EmployeeUser


@admin.register(EmployeeUser)
class EmployeeUserAdmin(UserAdmin):

    list_display = ('username', 'email', 'first_name', 'last_name', 'department', 'is_manager', 'is_staff')

    list_filter = ('department', 'is_manager', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        ('Professional Info', {'fields': ('job_title', 'department', 'is_manager', 'profile_picture')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Professional Info',
         {'fields': ('first_name', 'last_name', 'email', 'job_title', 'department', 'is_manager')}),
    )
