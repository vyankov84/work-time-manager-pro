from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse


UserModel = get_user_model()

class EmployeeUserTests(TestCase):

    def setUp(self):
        self.manager_user = UserModel.objects.create_user(
            username='manager',
            email='manager@company.com',
            password='123manager456',
            first_name='Sponge',
            last_name='Bob',
            is_manager=True,
        )

        self.regular_user = UserModel.objects.create_user(
            username='worker',
            email='worker@company.com',
            password='123worker456',
            first_name='Patrick',
            last_name='Star',
        )

    def test_user_string_represent(self):
        self.assertEqual(str(self.manager_user), 'Sponge Bob : (manager)')


    def test_email_validator_with_wrong_domain(self):
        user = UserModel(
            username='some',
            email='some@abv.com',
            first_name='Squidward',
            last_name='Tentacles'
        )

        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_employee_list_view_redirects(self):
        response = self.client.get(reverse('accounts:employee-list'))
        self.assertEqual(response.status_code, 302)

    def test_only_manager_access_update_view(self):
        self.client.login(username='worker', password='123worker456')
        url = reverse('accounts:employee-update', kwargs={'pk': self.manager_user.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)

    def test_login_process(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'manager',
            'password': '123manager456'
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue('_auth_user_id' in self.client.session)

