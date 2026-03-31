from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from decimal import Decimal
from clients.models import Client
from projects.models import Project
from projects.choices import RegionType

UserModel = get_user_model()

class ProjectTests(TestCase):

    def setUp(self):
        self.manager = UserModel.objects.create_user(
            username='final_boss',
            email='final_boss@company.com',
            password='password123',
            is_manager=True
        )

        self.client_obj = Client.objects.create(name="World Global", contact_email="wglobal@abv.com")

        self.project = Project.objects.create(
            name="Project One",
            job_number="1110000001",
            region=RegionType.EMEA,
            client=self.client_obj,
            project_manager=self.manager,
            estimated_hours=100,
            hourly_rate=Decimal('50.00')
        )

    def test_job_number_region_mismatch_fails(self):
        project = Project(
            name="Incorrect Project",
            job_number="1110000000",
            region=RegionType.APAC,
            client=self.client_obj
        )

        with self.assertRaises(ValidationError):
            project.full_clean()

    def test_progress_percentage_calculation(self):

        self.assertEqual(self.project.progress_percentage, 0)
        self.project.estimated_hours = 0
        self.assertEqual(self.project.progress_percentage, 0)

    def test_dashboard_context_data(self):
        self.client.login(username='final_boss', password='password123')
        response = self.client.get(reverse('projects:dashboard'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total_projects'], 1)
        self.assertEqual(response.context['page_title'], 'Dashboard')

    def test_project_detail_access(self):
        url = reverse('projects:project-details', kwargs={'pk': self.project.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_project_string_method(self):
        expected_str = f"Project One : 1110000001"
        self.assertEqual(str(self.project), expected_str)

