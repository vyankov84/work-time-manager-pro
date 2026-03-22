from django.db import models


class RegionType(models.TextChoices):
    EMEA = 'EMEA', 'EMEA'
    APAC = 'APAC', 'APAC'
    NA = 'NA', 'NA'
    LATAM = 'LATAM', 'LATAM'

class ProjectStatus(models.TextChoices):
    ACTIVE = 'ACTIVE', 'ACTIVE'
    PENDING = 'PENDING', 'PENDING'
    ON_HOLD = 'ONHOLD', 'ONHOLD'
    COMPLETED = 'COMPLETED', 'COMPLETED'

