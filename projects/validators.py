from django.core.exceptions import ValidationError

from projects.choices import RegionType

REGION_PREFIX = {
    RegionType.EMEA: '111',
    RegionType.APAC: '222',
    RegionType.NA: '333',
    RegionType.LATAM: '444',
}

def validate_job_number_region(job_number, region):

    expected = REGION_PREFIX.get(region)

    if expected and not job_number.startswith(expected):
        raise ValidationError(
            f'The region {region} is not valid for the job number {job_number}! The JN should start with {expected}.'
        )
