from django.db import models

class DepartmentType(models.TextChoices):

    ADMIN = 'Admin', 'Administration'
    HR = 'HR', 'Human Resources'
    FINANCE = 'Finance', 'Finance'
    LEGAL = 'Legal', 'Legal'
    SALES = 'Sales', 'Sales'
    IT = 'IT', 'Information Technology'
    DEV = 'Development', 'Development'
    QA = 'QA', 'Quality Assurance'
    PM = 'PM', 'Project Management'
    SUPPORT = 'Support', 'Customer Support'
    LOGISTICS = 'Logistics', 'Logistics'
    OTHER = 'Other', 'Other'
