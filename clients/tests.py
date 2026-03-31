from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from clients.models import Client

UserModel = get_user_model()

class ClientTests(TestCase):

    def setUp(self):
        self.manager = UserModel.objects.create_user(
            username='manager_user',
            email='manager@company.com',
            password='password123',
            is_manager=True
        )
        self.worker = UserModel.objects.create_user(
            username='worker_user',
            email='worker@company.com',
            password='password123',
            is_manager=False
        )

        self.client_obj = Client.objects.create(
            name="The Big Company",
            contact_person="Donald Duck",
            country="USA",
            contact_email="donald@yahoo.bg",
            phone_number="359888123456"
        )

    def test_client_string_representation(self):
        self.assertEqual(str(self.client_obj), "The Big Company")

    def test_phone_number_too_short_validation(self):
        client = Client(
            name='PineApple',
            contact_email='pine@hotmail.com',
            phone_number='123'
        )

        with self.assertRaises(ValidationError):
            client.full_clean()

    def test_only_manager_can_access_create_client(self):
        self.client.login(username='worker_user', password='password123')
        response = self.client.get(reverse('clients:client-create'))

        self.assertEqual(response.status_code, 403)

    def test_client_list_view_authenticated(self):
        self.client.login(username='worker_user', password='password123')
        response = self.client.get(reverse('clients:clients-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clients/clients-list.html')

    def test_delete_view_form_fields_are_disabled(self):
        self.client.login(username='manager_user', password='password123')
        url = reverse('clients:client-delete', kwargs={'pk': self.client_obj.pk})
        response = self.client.get(url)

        form = response.context['form']
        self.assertTrue(form.fields['name'].widget.attrs.get('disabled'))
        self.assertTrue(form.fields['contact_email'].widget.attrs.get('disabled'))

